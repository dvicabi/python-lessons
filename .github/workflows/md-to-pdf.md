name: MD ➜ PDF (GitHub style, RTL, Unicode, Auto Chrome)

on:
  push:
    branches: [ main ]
    paths:
      - '**.md'
  workflow_dispatch: {}

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies (Puppeteer + fonts)
        run: |
          sudo apt-get update
          sudo apt-get install -y xvfb fonts-noto fonts-noto-cjk fonts-noto-color-emoji fonts-dejavu-core culmus
          mkdir -p tools/mdpdf
          cd tools/mdpdf
          npm init -y
          npm install --save-exact puppeteer@22 md-to-pdf@5 github-markdown-css@5 highlight.js markdown-it markdown-it-footnote markdown-it-emoji

      - name: Write convert.js (force Chrome path)
        run: |
          cat > tools/mdpdf/convert.js << 'EOF'
          const fs = require('fs');
          const path = require('path');
          const puppeteer = require('puppeteer');
          const { mdToPdf } = require('md-to-pdf');
          const MarkdownIt = require('markdown-it');
          const hljs = require('highlight.js');
          
          // טעינה בטוחה של פלאגינים
          let mdFootnote, mdEmoji;
          try {
            mdFootnote = require('markdown-it-footnote');
            mdEmoji = require('markdown-it-emoji');
          } catch {
            console.warn('⚠️ markdown-it-footnote/emoji not loaded');
            mdFootnote = () => (md) => md;
            mdEmoji = () => (md) => md;
          }
          
          // הגדרה של MarkdownIt
          const md = new MarkdownIt({
            html: true,
            linkify: true,
            highlight: (code, lang) => {
              try {
                if (lang && hljs.getLanguage(lang)) {
                  return `<pre><code class="hljs language-${lang}">` +
                         hljs.highlight(code, { language: lang }).value +
                         '</code></pre>';
                }
              } catch {}
              return `<pre><code class="hljs">${code}</code></pre>`;
            }
          });
          md.use(mdFootnote());
          md.use(mdEmoji());
          
          // זיהוי עברית
          const isRTL = (s) => /[\u0590-\u05FF]/.test(s);
          
          function wrapHtml(body, rtl) {
            const dir = rtl ? 'rtl' : 'ltr';
            return `<!doctype html>
            <html dir="${dir}" lang="${rtl ? 'he' : 'en'}">
            <head>
              <meta charset="utf-8">
              <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
              <style>
                body { font-family: "Noto Sans Hebrew", "Noto Sans", sans-serif; }
                .markdown-body { box-sizing: border-box; padding: 20px; }
                html[dir=rtl] .markdown-body { direction: rtl; text-align: right; }
              </style>
            </head>
            <body><article class="markdown-body">${body}</article></body>
            </html>`;
          }
          
          function* walk(dir) {
            for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
              const f = path.join(dir, e.name);
              if (e.isDirectory()) yield* walk(f);
              else if (e.isFile() && f.endsWith('.md') && !f.includes('node_modules') && !f.includes('.git'))
                yield f;
            }
          }
          
          (async () => {
            const root = path.resolve(__dirname, '../..');
            const files = [...walk(root)];
            console.log('📄 Found', files.length, 'markdown files');
            let ok = 0, fail = 0;
          
            const browser = await puppeteer.launch({
              headless: true,
              args: ['--no-sandbox', '--disable-setuid-sandbox']
            });
          
            for (const file of files) {
              try {
                const mdText = fs.readFileSync(file, 'utf8');
                const html = wrapHtml(md.render(mdText), isRTL(mdText));
                const out = file.replace(/\.md$/, '.pdf');
          
                const res = await mdToPdf({ content: html }, {
                  launch_options: { args: ['--no-sandbox'], browser },
                  pdf_options: { format: 'A4', printBackground: true }
                });
          
                if (res && res.pdf) {
                  fs.writeFileSync(out, res.pdf);
                  console.log('✅', out);
                  ok++;
                } else {
                  console.log('⚠️ no PDF:', file);
                  fail++;
                }
              } catch (e) {
                console.error('❌', file, e.message);
                fail++;
              }
            }
          
            await browser.close();
            console.log('✅ OK:', ok, ' ❌ FAIL:', fail);
            if (ok === 0) process.exit(1);
          })();

          EOF

      - name: Run conversion under xvfb
        run: |
          cd tools/mdpdf
          xvfb-run -a node convert.js

      - name: Upload PDFs
        uses: actions/upload-artifact@v4
        with:
          name: md-pdfs
          path: '**/*.pdf'
          if-no-files-found: error

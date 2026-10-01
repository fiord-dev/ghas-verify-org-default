// PR 上で Code Scanning (CodeQL) に新規検出させるための、意図的に脆弱なサンプル。検証専用。
const fs = require("fs");
const http = require("http");
const url = require("url");

http
  .createServer((req, res) => {
    const q = url.parse(req.url, true).query;
    // Path traversal (js/path-injection)
    const body = fs.readFileSync("/srv/data/" + q.file, "utf8");
    // Code injection (js/code-injection)
    const result = eval(q.expr);
    res.end(body + String(result));
  })
  .listen(8081);

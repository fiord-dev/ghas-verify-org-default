"""PR 上で Code Scanning (CodeQL) に新規検出させるための、意図的に脆弱なコード。

main に存在しないルールを発生させる。検証専用。実行・デプロイしないこと。
"""
import requests
from flask import Blueprint, redirect, request

admin = Blueprint("admin", __name__)


@admin.route("/admin/eval")
def run_expr():
    # Code injection (py/code-injection)
    return str(eval(request.args.get("expr", "1+1")))


@admin.route("/admin/go")
def go():
    # Open redirect (py/url-redirection)
    return redirect(request.args.get("next", "/"))


@admin.route("/admin/fetch")
def fetch():
    # Server-side request forgery (py/full-ssrf)
    return requests.get(request.args.get("url", "")).text

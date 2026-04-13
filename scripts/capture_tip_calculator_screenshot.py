#!/usr/bin/env python3
"""Start the Tip Calculator briefly and save docs/screenshots/tip_calculator_running.png.

Requires: pip install playwright && playwright install chromium

Streamlit's first-run email prompt is skipped by using a temporary HOME with
``~/.streamlit/config.toml`` setting ``[server] headless = true`` (no credentials file).
"""

from __future__ import annotations

import os
import random
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def _write_streamlit_headless_config(home: Path) -> None:
    """Headless + no credentials file lets Streamlit skip the email prompt (see credentials.check_credentials)."""
    streamlit_dir = home / ".streamlit"
    streamlit_dir.mkdir(parents=True, exist_ok=True)
    (streamlit_dir / "config.toml").write_text(
        "[server]\nheadless = true\n",
        encoding="utf-8",
    )


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    png = root / "docs" / "screenshots" / "tip_calculator_running.png"
    png.parent.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Install Playwright first:\n"
            "  .venv/bin/pip install playwright\n"
            "  .venv/bin/python -m playwright install chromium",
            file=sys.stderr,
        )
        return 1

    port = random.randint(8800, 8999)
    fake_home = Path(tempfile.mkdtemp(prefix="streamlit_home_"))
    try:
        _write_streamlit_headless_config(fake_home)
        env = {
            **os.environ,
            "HOME": str(fake_home),
            "STREAMLIT_BROWSER_GATHER_USAGE_STATS": "false",
            "STREAMLIT_SERVER_FILE_WATCHER_TYPE": "none",
            "PYTHONUNBUFFERED": "1",
        }
        cmd = [
            sys.executable,
            "-u",
            "-m",
            "streamlit",
            "run",
            str(root / "app.py"),
            "--server.port",
            str(port),
            "--server.address",
            "127.0.0.1",
        ]
        proc = subprocess.Popen(
            cmd,
            cwd=str(root),
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        shutil.rmtree(fake_home, ignore_errors=True)
        raise
    try:
        time.sleep(8)
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.goto(f"http://127.0.0.1:{port}/", wait_until="domcontentloaded", timeout=120000)
            page.wait_for_timeout(5000)
            page.screenshot(path=str(png), full_page=True)
            browser.close()
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=12)
        except subprocess.TimeoutExpired:
            proc.kill()
        shutil.rmtree(fake_home, ignore_errors=True)

    if not png.is_file():
        print("Screenshot file was not created.", file=sys.stderr)
        return 1

    print(f"Saved {png}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

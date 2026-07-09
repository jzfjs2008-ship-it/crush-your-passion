"""Locale detection and translation helpers for bilingual (en/zh) support."""

import os
import re
import locale as _locale

# Detect Chinese characters in text
_HAS_CHINESE = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]').search


def detect_locale(text: str | None = None) -> str:
    """Detect user locale from input text or environment.

    Priority:
    1. Chinese chars in input text → zh
    2. LC_ALL / LANG / LANGUAGE env vars → zh if contains 'zh'
    3. Windows GetUserDefaultUILanguage fallback
    4. Default → en
    """
    if text and _HAS_CHINESE(text):
        return "zh"

    for var in ("LC_ALL", "LANG", "LANGUAGE"):
        val = os.environ.get(var, "")
        if "zh" in val.lower():
            return "zh"

    try:
        sys_lang, _ = _locale.getdefaultlocale()
        if sys_lang and "zh" in sys_lang:
            return "zh"
    except Exception:
        pass

    # Windows: check windll
    try:
        import ctypes
        lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
        # 0x0804 = zh-CN, 0x0404 = zh-TW, 0x0C04 = zh-HK
        if lang_id in (0x0804, 0x0404, 0x0C04):
            return "zh"
    except Exception:
        pass

    return "en"


def _t(en: str, zh: str, locale: str = "en") -> str:
    """Bilingual string — returns zh if locale is 'zh', else en."""
    return zh if locale == "zh" else en

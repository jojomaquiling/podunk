# ------------------------------------------------------------------------------
#   file:       podunk/widget/font.py
#   author:     Jim Storch (modified with TTF support, fallback, and optional styles)
# ------------------------------------------------------------------------------

import os
import warnings
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

"""
This class is designed so that the report coder can treat built-in and embedded
fonts in exactly the same manner. If you specify a path in the keyword dict
then it will load them from disk, otherwise it just holds names.
"""


class Font(object):

    def __init__(self, kwargs):
        self.plain = kwargs.get('plain')
        self.bold = kwargs.get('bold')
        self.italic = kwargs.get('italic')
        self.bold_italic = kwargs.get('bold_italic')

        if not self.plain:
            raise ValueError("The 'plain' font must be specified.")

        path = kwargs.get('path')
        if path:
            self.embed_font(path, self.plain)
            if self.bold:
                self.embed_font(path, self.bold)
            if self.italic:
                self.embed_font(path, self.italic)
            if self.bold_italic:
                self.embed_font(path, self.bold_italic)

    # ------------------------------------------------------------Embed Font

    def embed_font(self, path, face_name):
        """
        Register a font face with ReportLab and (if used) embed in the target PDF.
        Supports both TTF and Type 1 fonts. Logs a warning if font not found.
        """
        ttf_path = os.path.join(path, face_name + '.ttf')
        afm_path = os.path.join(path, face_name + '.afm')
        pfb_path = os.path.join(path, face_name + '.pfb')

        if os.path.isfile(ttf_path):
            try:
                pdfmetrics.registerFont(TTFont(face_name, ttf_path))
            except Exception as e:
                warnings.warn(
                    f"Failed to register TTF font '{face_name}': {e}")
        elif os.path.isfile(afm_path) and os.path.isfile(pfb_path):
            try:
                face = pdfmetrics.EmbeddedType1Face(afm_path, pfb_path)
                pdfmetrics.registerTypeFace(face)
                font = pdfmetrics.Font(face_name, face_name, 'WinAnsiEncoding')
                pdfmetrics.registerFont(font)
            except Exception as e:
                warnings.warn(
                    f"Failed to register Type1 font '{face_name}': {e}")
        else:
            warnings.warn(
                f"Font files not found for '{face_name}' in path '{path}'")

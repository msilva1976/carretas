import sqlite3

import pandas as pd
from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import tkinter.ttk as ttk
from reportlab  import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

cnv = canvas.Canvas("meu_PDF.pdf", pagesize=A4)
cnv.drawString(0,0,"teste")
cnv.save()
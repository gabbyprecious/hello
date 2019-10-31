# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 00:28:34 2019
@author: PRECIOUS
"""
from flask import Flask, render_template, request
from model import *

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    startload = 1
    if request.method == 'POST':
        sentence = str(request.form['text']) 
        report = paraphrase(sentence)       
        startload = 0
        return render_template('index.html', starter = startload, report=report)
    return render_template('index.html', starter = startload)
  

def paraphrase(sentence):
 #[x for x in synonymIfExists(sentence)]
 final = ' '.join([str(x) for x in synonymIfExists(sentence)])
 return final     


if __name__ == '__main__':
    app.run()

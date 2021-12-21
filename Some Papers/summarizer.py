import openai
import wget
import pathlib
import pdfplumber
import numpy as np


def getPaper(paper_url, filename="Entanglement_and_Non_Markovianity.pdf"):
    downloadedPaper = wget.download(paper_url, filename)
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)

    return downloadedPaperFilePath


def showPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:"
    openai.organization = "org-DGunXizhSnapSzgGJeDRXn6J"
    openai.api_key = "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"
    engine_list = openai.Engine.list()

    for page in paperContent:
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(
            engine="davinci",
            prompt=text,
            temperature=0.3,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"],
        )
        print(response["choices"][0]["text"])


paperContent = pdfplumber.open("./Entanglement_and_Non_Markovianity.pdf").pages
showPaperSummary(paperContent)

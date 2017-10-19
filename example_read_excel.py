import pandas as pd
import numpy as np
from openpyxl import load_workbook


def read(excelPath, basePath):
    readPath = basePath + excelPath + '.xlsx'
    df_data = pd.read_excel(readPath)

    return df_data["path"]

def write(excelPath, basePath, answerList):

    # list -> pandas
    df_answer = pd.DataFrame(answerList, columns=['answer'])

    # write
    overwritePath = basePath + excelPath + '.xlsx'
    book = load_workbook(overwritePath)
    writer = pd.ExcelWriter(overwritePath, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df_answer.to_excel(writer, startcol=3, index=False)
    writer.save()
    return 0

basePath = '/home/yufeng/overleaf/questionnaire/excel/'

data_lists = ['capsaicin_2016_Female_2-1',
              'capsaicin_2016_Female_3-1',
              'capsaicin_2016_Female_3-2',
              'capsaicin_2016_Male_2-1',
              'capsaicin_2016_Male_3-1',
              'capsaicin_2016_Male_3-2']

for i_data in data_lists:
    imgList = read(i_data, basePath=basePath)

    # answer
    answerList = np.zeros(imgList.shape, dtype=np.int32)

    write(i_data, basePath=basePath, answerList=answerList)




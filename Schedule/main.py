from Schedule import *
import io
import base64
import yaml
import matplotlib
matplotlib.use('Agg') # используем Agg - неинтерактивный бэкэнд, который записывает графики в файлы ( в нашем случае в последовательность байтов), без использования дисплея


# Минималистичный формат
yamlMin = yaml.safe_load("""
    x1Max: 95
    x2Max: 95
    lines:
    - "x1"                    
    - "1 + log2(x1)"
    points:
    - [[2, 2],[3, 3],[4, 4],[5, 5],[6, 6],[7, 7],[8, 8],[9, 9],[10, 10],[15, 15],[20, 20],[25, 25],[30, 30],

    - [[2, 2],[3, 3],[4, 3],[5, 4],[6, 4],[7, 4],[8, 4],[9, 5],[600, 11],[15, 5],[20, 6],[25, 6],[30, 6],[35, 7],
""")




from PIL import Image

if __name__ == '__main__':
    try:
        Schedule.MakePlot(yamlMin)
        base64Encode = Schedule.PlotToBase64()
        
        # decode image and display that
        base64Decode = base64.b64decode(base64Encode);
        bytesIO = io.BytesIO(base64Decode);
        img = Image.open(bytesIO)   
        img.show()

    except Schedule.Exception as err:
        print(err)
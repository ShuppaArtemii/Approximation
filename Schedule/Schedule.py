import io
import base64
import re
import numpy as np
import matplotlib.pyplot as plt

class Schedule:
    class Exception(Exception):
        pass;


    def MakePlot(data : dict):
        data = Schedule.__NormalizeInput(data);
        linesList  = data["lines"];
        pointsList = data["points"];
        
        # Check all expressions of lines allowed
        for line in linesList:
            if not Schedule.__IsExpressionAllowed(line["expression"]):
                expression = line["expression"]
                raise Schedule.Exception(f"Expression is not allowed: \"{expression}\"");
        
        # Make replacements 
        for i in range(len(linesList)):    
            linesList[i]["expression"] = Schedule.__MakeReplacements(linesList[i]["expression"])

            

        # Calc dimentions of all expressions and check that they fit into the limit
        uniqueVariables, xVariables = Schedule.__CalcDimentions(linesList)
        generalDimention = len(uniqueVariables)
        
        if generalDimention > 2:
            raise Exception(f"Unable to display plot. Incorrect dimension value: {generalDimention}")
        

        plot = Schedule.__MakePlot(generalDimention, data);
        if plot == None:
            raise Schedule.Exception(f"Can't display plot.")
        
        for i in range(len(pointsList)):
            plot.AddPoints(pointsList[i]["coordinates"], pointsList[i]["color"])

        for i in range(len(linesList)):
            plot.AddLine(linesList[i]["expression"], list(xVariables[i]), color=linesList[i]["color"])
            

    def PlotToBase64():
        bytesIO = io.BytesIO();
        plt.savefig(bytesIO, format='jpg');

        bytesIO.seek(0);
        base64Data = base64.b64encode(bytesIO.read());

        return base64Data;

    def __NormalizeInput(data : dict):
        # по умолчанию данные считаются пустыми, будет нарисован пустой график
        if data is None:
            data = dict()

        # по умолчанию заголовок считается пустым
        data["title"] = data.get("title", None)
        
        # обработка 'data["lines"]'
        data["lines"] = data.get("lines", []) # по умолчанию линии считаются пустыми
        data["lines"] = Schedule.__NormalizeLines(data["lines"])

        # обработка 'data["points"]'
        data["points"] = data.get("points", []) # по умолчанию точки считаются пустыми
        data["points"] = Schedule.__NormalizePoints(data["points"])

        ## по умолчанию минимальный предел вида осей равен 0
        data["x1Min"] = data.get("x1Min", 0)
        data["x2Min"] = data.get("x2Min", 0)

        return data

    def __NormalizeLines(lines : list):
        #  функция - проверка, что объект типа list[str]
        def Is_instance_list_of_str(obj):
            if obj and isinstance(obj, list): # obj is list
                return all(isinstance(elem, str) for elem in obj) # every obj[i] is str
            return False

        def Is_instance_list_of_dict(obj):
            if obj and isinstance(obj, list): # obj is list
                return all(isinstance(elem, dict) for elem in obj) # every obj[i] is dict
            return False

        # если значения data["lines"] - список строк, то преобразуем каждый элемент в подробный объект - dict
        #   с ключами: "expression" - строковое представление зависимости и "color" - значение цвета
        if Is_instance_list_of_str(lines):
            tmpLines = lines;
            lines = []
            for i in range(len(tmpLines)):
                lines.append({"expression": tmpLines[i], "color": None })
        
        # иначе проверяем что, все элементы - dict объекты с ключом "expression" и, возможно, "color" (по умолчанию цвет подбирается самостоятельно)
        elif Is_instance_list_of_dict(lines) and all("expression" in line for line in lines):
            tmpLines= lines;
            lines = []
            for i in range(len(tmpLines)):
                lines.append(tmpLines[i].get("color", None))
        
        else:
            raise Schedule.Exception("Unsupport data[\"lines\"] format")
        
        return lines

    def __NormalizePoints(points: list):
         #  функция - проверка, что объект типа list[list[list[]]]
        def Is_list_of_list_of_list_of_int(obj):
            if obj and isinstance(obj, list): # obj is list
                if all(isinstance(elem1, list) for elem1 in obj): # every obj[i] is list
                    return all(isinstance(elem2, list) for elem2 in [elem1 for elem1 in obj]) # every obj[i][j] is list
                         
                            
            return False

        def Is_instance_list_of_dict(obj):
            if obj and isinstance(obj, list): # obj is list
                return all(isinstance(elem, dict) for elem in obj) # every obj[i] is dict
            return False

        # если значения data["points"] - list[list[list[float]]], то преобразуем каждый элемент в подробный объект - dict
        #   с ключами: "coordinates" - строковое представление зависимости и "color" - значение цвета
        if Is_list_of_list_of_list_of_int(points):
            tmpPoints = points
            points = []
            for i in range(len(tmpPoints)):
                points.append({"coordinates": tmpPoints[i], "color": None })

        # иначе проверяем что, все элементы - dict объекты с ключом "coordinates" и, возможно, "color" (по умолчанию цвет подбирается самостоятельно)
        elif Is_instance_list_of_dict(points) and all("coordinates" in line for line in points):
            tmpPoints= points
            points = []
            for i in range(len(tmpPoints)):
                points.append({"coordinates": tmpPoints[i], "color": None })
        
        return points

    def __IsExpressionAllowed(expression : str):
        patternOneOf = "(" + ")|(".join(Schedule.allowedWords) + ")";
        for word in re.findall('[a-zA-Z]+\d*', expression, flags=re.IGNORECASE):
            if not re.match(patternOneOf, word):
                return False;

        return True;
    
    def __MakeReplacements(expression : str):
        for old, new in Schedule.replacements.items():
            pattern = re.compile(old, re.IGNORECASE);
            expression = pattern.sub(new, expression);

        return expression;
    
    def __CalcDimentions(expressions):
        
        allUniqueVariablesSet = set()
        allUniqueVariablesList = list()
        for expression in expressions:
            uniqueVariables = set(re.findall('x\d+', expression["expression"], flags=re.IGNORECASE))
            allUniqueVariablesList.append(uniqueVariables)
            allUniqueVariablesSet = set.union(allUniqueVariablesSet, uniqueVariables)
        

        return allUniqueVariablesSet, allUniqueVariablesList;

    
    def __MakePlot(dimention, data):
        if dimention == 0 or dimention == 1:
            return Schedule.__Plot2D(data)
        elif dimention == 2:
            return Schedule.__Plot3D(data)
        else:
            raise Exception(f"Unable to display plot. Incorrect dimension value: {dimention}")

    class __Plot2D:
        def __init__(self, data:dict):
            self.graphPlot = plt.axes([0.1, 0.1, 0.85, 0.85]);
            self.graphPlot.set_title(data["title"])
            
            if data.get("x1Max"):
                self.graphPlot.set_xlim(data.get("x1Min", 0), data.get("x1Max", None))
                
            if data.get("x2Max"):
                self.graphPlot.set_ylim(data.get("x2Min", 0), data.get("x2Max", None))
            
            # set the x-spine
            self.graphPlot.spines['left'].set_position('zero')

            # turn off the right spine/ticks
            self.graphPlot.spines['right'].set_color('none')
            self.graphPlot.yaxis.tick_left()

             # set the y-spine
            self.graphPlot.spines['bottom'].set_position('zero')

            # turn off the top spine/ticks
            self.graphPlot.spines['top'].set_color('none')
            self.graphPlot.xaxis.tick_bottom()


        def AddLine(self, expression : str, xVarialbles, color):
            xMin, xMax = self.graphPlot.get_xlim()
            size = 50
            
            x = np.linspace(round(xMin), round(xMax), size);
            func = self.__GetFunc(expression, xVarialbles);
            
            if len(xVarialbles) == 0:
                y = size * [func()]
                self.graphPlot.plot(x, y, c=color, zorder=1);

            elif len(xVarialbles) == 1:
                y = func(x)
                self.graphPlot.plot(x, y, c=color, zorder=1);

            else:
                raise Schedule.Exception("Unable to display plot. Incorrect dimension value: {len(xVarialbles)}");

        def AddPoints(self, points, color):
            x1 = [row[0] for row in points]
            y = [row[1] for row in points]
            self.graphPlot.scatter(x1, y, c=color, zorder=2);


        def __GetFunc(self, expression : str, xVarialbles : list):
            def constFunc():
                return float(expression)
        
            def unaryFunc(x):
                exec(f"{xVarialbles[0]} = x")
                return eval(expression)

            if len(xVarialbles) == 0:
                return constFunc;
            elif len(xVarialbles) == 1:
                return unaryFunc;
            else:
                raise Schedule.Exception("Unable to display plot. Incorrect dimension value: {len(xVarialbles)}!");
    
    
    class __Plot3D:
        def __init__(self, data:dict):
            self.graphPlot = plt.axes([0.05, 0.05, 0.9, 0.9], projection='3d')
            self.graphPlot.set_title(data["title"])    
        
            self.graphPlot.set_xlim(data["x1Min"], data["x1Max"])
            self.graphPlot.set_ylim(data["x2Min"], data["x2Max"])
            
           
        def AddLine(self, expression : str, xVarialbles, color):
            x1Min, x1Max = self.graphPlot.get_xlim()
            x2Min, x2Max = self.graphPlot.get_ylim()
            size = 50
            x1Arr = np.linspace(x1Min, x1Max, size);
            x2Arr = np.linspace(x2Min, x2Max, size);
            x1grid, x2grid = np.meshgrid(x1Arr, x2Arr);
            func = self.__GetFunc(expression, xVarialbles);
            
            if len(xVarialbles) == 0:
                y = size * [func()]
                self.graphPlot.plot3D(x1grid, x2grid, y, c=color, zorder=1);

            elif len(xVarialbles) == 1:
                y = func(x1grid)
                self.graphPlot.plot3D(x1grid, x2grid, y, c=color, zorder=1);

            elif len(xVarialbles) == 2:

                
           
                x1grid, x2grid = np.meshgrid(x1Arr, x2Arr);
                func = self.__GetFunc(expression, xVarialbles);
                y = func(x1grid, x2grid)
                self.graphPlot.plot_surface(x1grid, x2grid, y)
            

            else:
                raise Schedule.Exception("Unable to display plot. Incorrect dimension value: {len(xVarialbles)}");


        def AddPoints(self, points, color):
            x1 = [row[0] for row in points]
            y = [row[1] for row in points]
            self.graphPlot.scatter(x1, y, c=color, zorder=2);


        def __GetFunc(self, expression : str, xVarialbles : list):
            def constFunc():
                return float(expression)
        
            def unaryFunc(x):
                exec(f"{xVarialbles[0]} = x")
                return eval(expression)
            
            def binaryFunc(x, y):
                exec(f"{xVarialbles[0]} = x")
                exec(f"{xVarialbles[1]} = y")
                return eval(expression)


            if len(xVarialbles) == 0:
                return constFunc;
            elif len(xVarialbles) == 1:
                return unaryFunc;
            elif len(xVarialbles) == 2:
                return binaryFunc;
            else:
                raise Schedule.Exception("Unable to display plot. Incorrect dimension value: {len(xVarialbles)}");

    allowedWords = [
        'x\d+',
        'exp',
        'log2',
        'ceil'
    ];
   
    replacements = {
        '\^': '**',
        'exp': 'np.exp',
        'log2': 'np.log2',
        'ceil': 'np.ceil'
    };
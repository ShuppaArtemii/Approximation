from Approximation.GuessApproximation import GuessApproximation
from Approximation.OutputData import OutputData
import yaml


def ApproximateAlgorithmWidthAndHeight(**kwargs):
    def ArgsHaveAllFrom(args, allowed_keys):
        for key in allowed_keys:
            if not key in args:
                return False;
        return True
    
    
    if ArgsHaveAllFrom(kwargs, ["dimentions", "iterations", "processors", "ticks"]):
        #merge "dimentions" and "iterations" into "parameters" 
        kwargs["parameters"] = []
        for i in range(len(kwargs["dimentions"])):
            row = kwargs["dimentions"][i].copy()
            row.append(kwargs["iterations"][i])
            kwargs["parameters"].append(row)
        kwargs.pop("dimentions", None)
        kwargs.pop("iterations", None)

    if ArgsHaveAllFrom(kwargs, ["parameters", "processors", "ticks"]):
        width_koeff, width_func, width_disc = GuessApproximation.Analyse(kwargs["parameters"], kwargs["processors"], fastMode=True)
    
        height_koeff, height_func, height_disc = GuessApproximation.Analyse(kwargs["parameters"], kwargs["ticks"], fastMode=True)
    
        return OutputData(width_koeff, width_func, height_koeff, height_func)

    else:
        return OutputData([],[],[],[])

def ProcessAlgorithmWidthAndHeight(dimentions, iterations, processors, ticks):
    #merge parameters 
    parameters = []
    for i in range(len(dimentions)):
        row = dimentions[i].copy()
        row.append(iterations[i])
        parameters.append(row)

    width_koeff, width_func, width_disc = GuessApproximation.Analyse(parameters, processors, fastMode=True)
    
    height_koeff, height_func, height_disc = GuessApproximation.Analyse(parameters, ticks, fastMode=True)
    
    ouputData = OutputData(width_koeff, width_func, height_koeff, height_func)
    return ouputData




if __name__ == '__main__':
    example1 = yaml.safe_load("""
        dimentions: [[1],[2],[3],[4],[5]]
        iterations: [0, 0, 0, 0, 0]
        processors: [3, 6, 9, 12, 15]
        ticks: [1, 2, 3, 4, 5]
    """)
    outputData = ApproximateAlgorithmWidthAndHeight(**example1).data
    print(outputData)

    example2 = yaml.safe_load("""
        parameters:[
            [1, 0],
            [2, 0],
            [3, 0],
            [4, 0],
            [5, 0]
        ]
        processors:[
            3, 6, 9, 12, 15
        ]
        ticks:[
            1, 2, 3, 4, 5
        ]
    """)
    outputData = ApproximateAlgorithmWidthAndHeight(**example1).data
    print(outputData)

from Approximation import GuessApproximation
from Schedule import Schedule
from Approximation import FunctorListMethods


if __name__ == '__main__':
    #y = 1 + log2(x0)
    parameters = [[2],[3],[4],[5],[6],[7],[8],[9],[15],[20],[25],[30],[35],[40],[45],[50],[100],[150],[200],[250],[300],[350],[400],[450],[500]];
    results = [2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 10, 10, 10, 10, 10];
    
    koefficients, functorsList, discripancy = GuessApproximation.GuessApproximation.Analyse(parameters, results);
    print(FunctorListMethods.GetStringInfo(koefficients, functorsList, discripancy));
    Schedule.Schedule.Draw(koefficients, functorsList, 1, 100);

    #y = 3*x0
    parameters = [[2], [3], [4], [5]];
    results = [6, 9, 12, 15];
    
    koefficients, functorsList, discripancy = GuessApproximation.GuessApproximation.Analyse(parameters, results);
    print(FunctorListMethods.GetStringInfo(koefficients, functorsList, discripancy));
    Schedule.Schedule.Draw(koefficients, functorsList, 0, 100);
    
    #z = x^2 + y^2
    parameters = [[-5,-5],[-5,-4],[-5,-3],[-5,-2],[-5,-1],[-5,-0],[-5,1],[-5,2],[-5,3],[-5,4],[-5,5],
                       [-4,-5],[-4,-4],[-4,-3],[-4,-2],[-4,-1],[-4,-0],[-4,1],[-4,2],[-4,3],[-4,4],[-4,5],
                       [-3,-5],[-3,-4],[-3,-3],[-3,-2],[-3,-1],[-3,-0],[-3,1],[-3,2],[-3,3],[-3,4],[-3,5],
                       [-2,-5],[-2,-4],[-2,-3],[-2,-2],[-2,-1],[-2,-0],[-2,1],[-2,2],[-2,3],[-2,4],[-2,5],
                       [-1,-5],[-1,-4],[-1,-3],[-1,-2],[-1,-1],[-1,-0],[-1,1],[-1,2],[-1,3],[-1,4],[-1,5],
                       [0,-5],[0,-4],[0,-3],[0,-2],[0,-1],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],
                       [1,-5],[1,-4],[1,-3],[1,-2],[1,-1],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],
                       [2,-5],[2,-4],[2,-3],[2,-2],[2,-1],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],
                       [3,-5],[3,-4],[3,-3],[3,-2],[3,-1],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],
                       [4,-5],[4,-4],[4,-3],[4,-2],[4,-1],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],
                       [5,-5],[5,-4],[5,-3],[5,-2],[5,-1],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]];
    results = [50,41,34,29,26,25,26,29,34,41,50,41,32,25,20,17,16,17,20,25,32,41,34,25,18,13,10,9,10,13,18,25,34,29,20,13,8,5,4,5,8,13,20,29,26,17,10,5,2,1,2,5,10,17,26,25,16,9,4,1,0,1,4,9,16,25,26,17,10,5,2,1,2,5,10,17,26,29,20,13,8,5,4,5,8,13,20,29,34,25,18,13,10,9,10,13,18,25,34,41,32,25,20,17,16,17,20,25,32,41,50,41,34,29,26,25,26,29,34,41,50];
           

    koefficients, functorsList, discripancy = GuessApproximation.GuessApproximation.Analyse(parameters, results);
    print(FunctorListMethods.GetStringInfo(koefficients, functorsList, discripancy));
    Schedule.Schedule.Draw(koefficients, functorsList, 0, 11, 1);
import unittest
from Approximation.AutoApproximation import AutoApproximation
from Approximation.Instruments.Functors.Const import Const
from Approximation.Instruments.Functors.X import X
from Approximation.Instruments.Functors.Power import Power
from Approximation.Instruments.Functors.Log2 import Log2
from Approximation.Instruments.Functors.Ceil import Ceil
from Approximation.Instruments.Functors.Exp import Exp
from Approximation.Instruments.FunctorList.Sum import Sum
from Approximation.Instruments.FunctorList.Multiplication import Multiplication
from Approximation.Instruments.Sequences.PowerMultiplySequence import PowerMultiplySequence


class testAutoApproximation(unittest.TestCase):
    def test_11(self):
        parameters = [[0]];
        results = [11];

        expectedKoefficients = [11];
        expectedFunctorList = Sum(Multiplication([Const()]));
        expectedDiscripancy = 0;
        
        actualKoefficients, actualFunctorList, actualDiscripancy = AutoApproximation.Analyse(
            parameters, results, fastMode=False, fullBustMode=False, debugMode=False);

        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");
        self.assertEqual(actualFunctorList, expectedFunctorList, "actualFunctorList != expectedFunctorList");
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");

    def test_x(self):
        parameters = [[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5]];
        results = [-5, -4, -3,-2,-1, 0, 1, 2, 3, 4, 5];
        
        expectedKoefficients = [1];
        expectedFunctorList = PowerMultiplySequence.GetSequence([X(0)], 1, 2);
        expectedDiscripancy = 0;
        
        actualKoefficients, actualFunctorList, actualDiscripancy = AutoApproximation.Analyse(
            parameters, results, fastMode=False, fullBustMode=False, debugMode=False);
                
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");
        print(f"actualFunctorList: {actualFunctorList.ToString()}")
        self.assertEqual(actualFunctorList, expectedFunctorList, "actualFunctorList != expectedFunctorList");
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");
    
    def test_small_log2x(self):
        parameters = [[1],[2],[3],[4],[5]];
        results = [0, 1, 2, 2, 3];
        
        expectedKoefficients = [1];
        #expectedFunctorList = Sequences.PowerSequence.PowerSequence.GetSequence([Functors.CeilFunctor.CeilFunctor(Functors.BaseFunctor.BaseFunctor(Functions.Log2X, [0], "log2(x0)"))], 1, 2);
        expectedDiscripancy = 0;
        
        actualKoefficients, actualFunctorList, actualDiscripancy = AutoApproximation.Analyse(
            parameters, results, fastMode=False, fullBustMode=False, debugMode=False, baseFunctorList=self.__Log2First());
        
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");
        print(f"actualFunctorList: {actualFunctorList.ToString()}")
        #self.assertEqual(actualFunctorList, expectedFunctorList, "actualFunctorList != expectedFunctorList");
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");
        
     
    def test_1_plus_log2x(self):
        parameters = [[2],[3],[4],[5],[6],[7],[8],[9],[15],[20],[25],[30],[35],[40],[45],[50],[100],[150],[200],[250],[300],[350],[400],[450],[500]];
        results = [2,3,3,4,4,4,4,5,5,6,6,6,7,7,7,7,8,9,9,9,10,10,10,10,10];
        
        expectedKoefficients = [1, 1];
        #expectedFunctorList = [];
        #expectedFunctorList.append(Functors.BaseFunctor.BaseFunctor(Functions.Return1, [], ""));
        #expectedFunctorList.extend(Sequences.PowerSequence.PowerSequence.GetSequence([Functors.CeilFunctor.CeilFunctor(Functors.BaseFunctor.BaseFunctor(Functions.Log2X, [0], "log2(x0)"))], 1, 2));
        expectedDiscripancy = 0;
        
        actualKoefficients, actualFunctorList, actualDiscripancy = AutoApproximation.Analyse(
            parameters, results, fastMode=False, fullBustMode=False, debugMode=False, baseFunctorList=self.__Log2First());
        for j in range(len(actualKoefficients)):
            actualKoefficients[j] = round(actualKoefficients[j]);
        
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");
        print(f"actualFunctorList: {actualFunctorList.ToString()}")
        #self.assertEqual(actualFunctorList, expectedFunctorList, "actualFunctorList != expectedFunctorList");
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");
    
    def __Log2First(self):
        return [[Ceil(Log2(X(0)))], [X(0)], [Ceil(Exp(X(0)))]];


    def test_x_pow2_plus_y_pow_2(self):
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
         
        expectedKoefficients = [1, 1];
        #expectedFunctorList = [];
        #expectedFunctorList.extend(Sequences.PowerSequence.PowerSequence.GetSequence([Functors.BaseFunctor.BaseFunctor(Functions.ReturnX, [0], "x0")], 2, 3));
        #expectedFunctorList.extend(Sequences.PowerSequence.PowerSequence.GetSequence([Functors.BaseFunctor.BaseFunctor(Functions.ReturnX, [1], "x1")], 2, 3));
         
        expectedDiscripancy = 0;
        
        actualKoefficients, actualFunctorList, actualDiscripancy = AutoApproximation.Analyse(parameters, results, fastMode=True, fullBustMode=False, debugMode=False);
        for j in range(len(actualKoefficients)):
            actualKoefficients[j] = round(actualKoefficients[j]);
        
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");
        
        print(f"actualFunctorList: {actualFunctorList.ToString()}")
        #self.assertEqual(actualFunctorList, expectedFunctorList, "actualFunctorList != expectedFunctorList");
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");
    
    def test_expX(self):
        parameters = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]];
        results = [1,
            2.71828182845904,
            7.38905609893065,
            20.0855369231877,
            54.5981500331442,
            148.413159102577,
            403.428793492735,
            1096.63315842846,
            2980.95798704173,
            8103.08392757538,
            22026.4657948067,
            59874.1417151978
        ];
        expectedKoefficients = [1];
        expectedDiscripancy = 0.;

        actualKoefficients, actualFunctorList, actualDiscripancy = AutoApproximation.Analyse(
            parameters, results, fastMode=False, fullBustMode=False, debugMode=False, baseFunctorList=self.ExpFirst());
                
        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");
        print(f"actualFunctorList: {actualFunctorList.ToString()}")
        #self.assertEqual(actualFunctorList, expectedFunctorList, "actualFunctorList != expectedFunctorList");
        self.assertEqual(actualDiscripancy, expectedDiscripancy, "actualDiscripancy != expectedDiscripancy");


        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, msg="actualDiscripancy != expectedDiscripancy");

    def test_ceilExpX(self):
        parameters = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]];
        results = [3, 8, 21, 55, 149, 404, 1097, 2981, 8104, 22027, 59875];
        
        expectedKoefficients = [1];
        expectedDiscripancy = 0.;

        actualKoefficients, actualFunctorList, actualDiscripancy = AutoApproximation.Analyse(
            parameters, results, fastMode=False, fullBustMode=False, debugMode=False, baseFunctorList=self.ExpFirst());

        self.assertEqual(actualKoefficients, expectedKoefficients, "actualKoefficients != expectedKoefficients");
        print(f"actualFunctorList: {actualFunctorList.ToString()}")
        self.assertAlmostEqual(actualDiscripancy, expectedDiscripancy, msg="actualDiscripancy != expectedDiscripancy");

        
    def ExpFirst(self):
        return [[Ceil(Exp(X(0)))], [Ceil(Log2(X(0)))], [X(0)]];

if __name__ == '__main__':
    unittest.main()

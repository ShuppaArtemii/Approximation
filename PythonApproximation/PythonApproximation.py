
class Approximation:
	def __init__(self):
		pass;

	def __init__(self, parameters):
		self.SetParameters(parameters);
	
	def __init__(self, parameters, results):
		self.SetParameters(parameters);
		self.SetResults(results);

	#Setters
	def SetParameters(self, parameters):
		self.parameters = parameters;
		
	def SetResults(self, results):
		self.results = results;
		
	#like public methods
	def CalcKoefficients(self, functions, conformity):
		calcMatrix_ = self.InitializeCalcMatrix_(functions, conformity);
		koefficients = self.SolveCalcMatrix_(calcMatrix_);
		return koefficients;

	def CalcDiscripancy(self, koefficients, functions, conformity):
		height_ = len(self.parameters);
		width_ = len(self.parameters[0]);
		squareDiscripancySum = 0;

		for rowIdx in range(0, height_):
			sum = 0;
			for colIdx in range(width_, 0, - 1):
				for funcIdx in range(len(functions)):
					sum += koefficients[funcIdx] * functions[funcIdx](self.GetFunctionParameters_(funcIdx, rowIdx, conformity));
					#value = koefficients[colIdx] * functions[colIdx](self.GetFunctionParameters_(colIdx, rowIdx, conformity));
			disc = self.results[rowIdx] - sum;
			squareDiscripancySum += disc * disc;

		return squareDiscripancySum;
	
	def GetFunctionParameters_(self, funcIdx, rowIdx, conformity):
		row = [];
		for i in range(0, len(conformity[funcIdx])):
			row.append(self.parameters[rowIdx][i]);

		return row;

	#like protected methods
	def InitializeCalcMatrix_(self, functions, conformity):
		calcMatrix_ = [];
		
		for funcIdx1 in range(len(functions)):
			row = [];
			for funcIdx2 in range(len(functions)):
				colomnSum = 0;
				for rowIdx in range(0, len(self.parameters)):
					colomnSum += functions[funcIdx1](self.GetFunctionParameters_(funcIdx1, rowIdx, conformity)) * functions[funcIdx2](self.GetFunctionParameters_(funcIdx2, rowIdx, conformity));
				row.append(colomnSum);
			
			colomnSum = 0;
			for rowIdx in range(0, len(self.parameters)):
				colomnSum += self.results[rowIdx] * functions[funcIdx1](self.GetFunctionParameters_(funcIdx1, rowIdx, conformity));	
			row.append(colomnSum);
			calcMatrix_.append(row);
			
		return calcMatrix_;

	def SolveCalcMatrix_(self, calcMatrix_):
		height_ = len(calcMatrix_);
		width_ = len(calcMatrix_[0]);

		self.ToUpperTriangularView_(calcMatrix_, height_, width_);
		koefficients_ = [];
		for rowIdx in range(height_ - 1, -1, -1):
			rowSum = 0;
			for k in range(0, width_):
				rowSum += calcMatrix_[rowIdx][k];

			koeff = 2 * calcMatrix_[rowIdx][height_] + 1 - rowSum;
			koefficients_.insert(rowIdx, koeff);
			for colIdx in range(0, rowIdx):
				calcMatrix_[colIdx][rowIdx] *= koeff;

		return koefficients_;

	def ToUpperTriangularView_(self, calcMatrix_, height_, width_):
		for i in range(0, height_):
			for j in range(i, height_):
				if(i == j):
					value = calcMatrix_[i][j];
					for k in range(0, width_):
						calcMatrix_[i][k] /= value;
				
				elif (i < j):
					multipleValue = calcMatrix_[j][i];
					tmpRow = [];
					for k in range(0, width_):
						tmpRow.append(calcMatrix_[i][k] * multipleValue);

					for k in range(0, width_):
						calcMatrix_[j][k] -= tmpRow[k];
						
		return;

def Return1(list):
	return 1;

def ReturnX(list):
	return list[0];

if __name__ == '__main__':
	parameters = [
		[2, 0], [3, 0], [4, 0], [5, 0]
	];
	processors = [6, 9, 12, 15];
	ticks = [4, 233, 5016, 128772];

	functions = [Return1, ReturnX];#тип регрессии, в данном случае он равен (y = a + b*x)
	conformity = [[], [0]];
	
	approximation = Approximation(parameters, processors);
	koefficients = approximation.CalcKoefficients(functions, conformity);
	discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);
	
	print("Processors");
	print("Koefficients: ", koefficients);
	print("Discripancy: ", discripancy);
	print();

	approximation.SetResults(ticks);
	koefficients = approximation.CalcKoefficients(functions, conformity);
	discripancy = approximation.CalcDiscripancy(koefficients, functions, conformity);

	print("Ticks");
	print("Koefficients: ", koefficients);
	print("Discripancy: ", discripancy);
	print();
import sys

class Hypothesis:
	def __init__(self,prior,cherry,lime):
		self.prior=prior
		self.cherry=cherry
		self.lime=lime

def main():
	if (len(sys.argv)>2):
		print'Incorrect Command'
		sys.exit(0)
	resultFile=open('result.txt', 'w')
	h1=Hypothesis(0.1,1.0,0.0)
	h2=Hypothesis(0.2,0.75,0.25)
	h3=Hypothesis(0.4,0.5,0.5)
	h4=Hypothesis(0.2,0.25,0.75)
	h5=Hypothesis(0.1,0.0,1.0)
	
	if (len(sys.argv)!=2):
		try:
			resultFile.write('Observation sequence Q: \n');
			resultFile.write('Length of Q: 0\n\n');
			resultFile.write("P(h1 | Q0) = %.5f \n" %(h1.prior))
			resultFile.write("P(h2 | Q0) = %.5f \n" %(h2.prior))
			resultFile.write("P(h3 | Q0) = %.5f \n" %(h3.prior))
			resultFile.write("P(h4 | Q0) = %.5f \n" %(h4.prior))
			resultFile.write("P(h5 | Q0) = %.5f \n\n" %(h5.prior))
			resultFile.write("Probability that the next candy we pick will be Cherry, given Q: 0.50000\n")
			resultFile.write("Probability that the next candy we pick will be Lime, given Q: 0.50000\n")
			resultFile.close()
		except Exception:
			print 'Error creating a file'
			resultFile.close()
		sys.exit(0)
	obseq=sys.argv[1] 
	length=len(obseq)
	new_prior=0.0
	qC=0.0
	qL=0.0
	resultFile.write('Observation sequence Q: ' + obseq + '\n');
        resultFile.write('Length of Q: ' + str(length) + '\n\n');
	for i in range(0,length):
                resultFile.write('After Observation Q'+ str(i+1) + ' = ' + obseq[i] + '\n');
                resultFile.write('\n');
		qC=(h1.prior*h1.cherry)+(h2.prior*h2.cherry)+(h3.prior*h3.cherry)+(h4.prior*h4.cherry)+(h5.prior*h5.cherry)
		qL=(h1.prior*h1.lime)+(h2.prior*h2.lime)+(h3.prior*h3.lime)+(h4.prior*h4.lime)+(h5.prior*h5.lime)
		if(obseq[i]=='c' or obseq[i]=='C'):
			new_prior=((h1.cherry*h1.prior)/qC);
			h1.prior=new_prior
			new_prior=((h2.cherry*h2.prior)/qC);
			h2.prior=new_prior
			new_prior=((h3.cherry*h3.prior)/qC);
			h3.prior=new_prior
			new_prior=((h4.cherry*h4.prior)/qC);
			h4.prior=new_prior
			new_prior=((h5.cherry*h5.prior)/qC);
			h5.prior=new_prior
		elif (obseq[i]=='l' or obseq[i]=='L'):
			new_prior=((h1.lime*h1.prior)/qL);
			h1.prior=new_prior
			new_prior=((h2.lime*h2.prior)/qL);
			h2.prior=new_prior
			new_prior=((h3.lime*h3.prior)/qL);
			h3.prior = new_prior
			new_prior=((h4.lime*h4.prior)/qL);
			h4.prior=new_prior
			new_prior=((h5.lime*h5.prior)/qL);
			h5.prior=new_prior
		else:
			print'Incorrect Inputs'
			resultFile.close();
		        sys.exit(0)
                qC=(h1.prior*h1.cherry)+(h2.prior*h2.cherry)+(h3.prior*h3.cherry)+(h4.prior*h4.cherry)+(h5.prior*h5.cherry)
                qL=(h1.prior*h1.lime)+(h2.prior*h2.lime)+(h3.prior*h3.lime)+(h4.prior*h4.lime)+(h5.prior*h5.lime)
                try:
                        resultFile.write("P" +str(i+1) + "(h1 | Q" + str(i+1) + ") = %.5f \n" %(h1.prior))
                        resultFile.write("P" + str(i+1) + "(h2 | Q" + str(i+1) + ") = %.5f \n" %(h2.prior))
                        resultFile.write("P" + str(i+1) + "(h3 | Q" + str(i+1) + ") = %.5f \n" %(h3.prior))
                        resultFile.write("P" + str(i+1) + "(h4 | Q" + str(i+1) + ") = %.5f \n" %(h4.prior))
                        resultFile.write("P" + str(i+1) + "(h5 | Q" + str(i+1) + ") = %.5f \n\n" %(h5.prior))
                        resultFile.write("Probability that the next candy we pick will be Cherry, given Q" + str(i+1) + ": %.5f \n" %(qC))
                        resultFile.write("Probability that the next candy we pick will be Lime, given Q" + str(i+1) + ": %.5f \n" %(qL))
                        resultFile.write('\n');
                except Exception:
                        print'Error creating a file'
                        resultFile.close()

if (__name__ == '__main__'):
	main()

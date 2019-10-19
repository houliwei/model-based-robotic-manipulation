class ImpedanceControl:
	def __init__(self):
		self.Md = 0
		self.Bd = 0
		self.Kd = 0
		self.Initialize()

	def Initialize(self):
		#set time variable
		import time
		self.currtm = time.time()
		self.prevtm = self.currtm
		NoT = 0  #number of cycle
	
	def SetMd(self,MdInput):
		self.Md = MdInput
	def SetBd(self,BdInput):
		self.Bd = BdInput
	def SetKd(self,KdInput):
		self.Kd = KdInput

	def GenOut(self,PPerror,Perror,Cerror,PPdeltaX,PdeltaX):
		Omega1 = 4*self.Md + 2*self.Bd*T + self.Kd*(T**2)
		Omega2 = -8*self.Md + 2*self.Kd*(T**2)
		Omega3 = 4*self.Md - 2*self.Bd*T + self.Kd*(T**2)
		if NoT == 1:
			return T**2 / Omega1 * Cerror
		elif NoT == 2:
			return T**2 / Omega1 * (Cerror + 2*Perror) - Omega2/Omega1*PdeltaX
		else:
			return T**2 / Omega1 *(Cerror + 2*Perror + PPerror) - (Omega2/Omega1)*PdeltaX - (Omega3/Omega1)*PPdeltaX


if __name__=="__main__":
	import numpy as np
	import matplotlib.pyplot as plt
	import time
	# creat an instance
	IC = ImpedanceControl()
	IC.SetMd(2.6)     ###
	IC.SetBd(1)   ###
	IC.SetKd(1)    ###
	T = 0.01
	Ke = 20    ### stiffness of the environment
	NoT = 1
	ErrorList = []
	XList = []
	Fd = 5   ###### target force
	pperror,perror,error,errorabs = 0,0,5,5     ### inital error == 5
	deltax,ppdeltax,pdeltax = 0,0,0
	flag=1   # if flag >= 1000, break
	while errorabs > 0.1 :
		begin = time.time()  
		time.sleep( (T-time.time()+begin) if time.time()-begin<T else 0.0)  # T=0.1
		deltax = IC.GenOut(PPerror=pperror,Perror=perror,Cerror=error,PPdeltaX=ppdeltax,PdeltaX=pdeltax)
		# prepare for next loop
		XList.append(deltax)
		ppdeltax = pdeltax
		pdeltax = deltax
		pperror = perror
		perror = error
		error = error-Ke*deltax
		errorabs = abs(error)
		ErrorList.append(error)
		NoT += 1
		flag += 1
		if flag == 100 :
    			break
# map
	plt.figure()
	plt.plot(XList,color='black',label='x', linewidth=1)
	plt.plot(ErrorList,color='red',label='error', linewidth=1)
	plt.legend()
	plt.show()
#print(ErrorList)





import numpy as np
#ejemplos de matrices 
v=[[1,0,2,0], [3,-1,5,4],[2,1,3,3],[3,4,5,6]]
x= []
o=[[5,3,5,2],[-2,-4,-3,-3],[3,0,3,-1],[-2,-5,1,-3]]
n=(10*np.random.randn( 8, 8 ))
z=[[2,-1,-4,-1,-2,-3,2,1], [-1,-2,-2,-1,3,4,-2,3], [0,2,4,-2,3,0,5,-3], [1,-4,4,1,1,1,2,-2], [1,0,5,-1,5,4,-1,-2],[-4,2,-4,-2,-3,-4,5,-4],[-1,5,-1,-3,5,2,0,5],[1,1,-3,-4,-2,-4,-1,-2] ] 

#sacar el determinante de la matriz inicial:
print(np.linalg.det(z))

p1=[]
p2=[]
#para separar la matrices en matrices menores con el metodo de cofactores 
class matriz:
	def __init__ (self, m):
		self.p=[]
		f=0
		l=[]
		r=[]
		for i in m:
			p1.append(i[0])
			del i[0] 
			l.append(i)
		for i in range (len(l)):
			r=list(l)
			del l[i]
			self.p.append(l)
			l=r
			
print ("matriz original:")		
for i in z:
	print(i) 			

#para mostrar las matrices 
class printe:
	def __init__ (self ,p,n):
		for i in range(len(p)):
			print("matriz",n,",",i+1,":  ")
			#para sacar el determinante de cada matriz
			for x in p[i]:
				print(x)
				r=np.linalg.det(p[i])
			print("det: ",r)
			k=r*p1[i]
			p2.append(int(k))
			print("det2: ",p1[i], k)
			
#en m se pone la matriz en la cual quieres trabajar y el.numero de la matriz (para clasificarla) y en ml se pone la salida de la matriz anterior m.p 
m1=matriz(z)
ml1=printe(m1.p, 7)
m2= matriz(m1.p[0])
ml2=printe(m2.p, 6)
m3= matriz(m2.p[0])
ml3=printe(m3.p, 5)
m4= matriz(m3.p[0])
ml4=printe(m4.p, 4)
m5= matriz(m4.p[0])
ml5=printe(m5.p, 3)

#este codigo fue originalmente escrito pot Imanol Elizondo :)

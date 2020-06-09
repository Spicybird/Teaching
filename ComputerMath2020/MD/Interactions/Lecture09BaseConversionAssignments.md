# **第09讲 基底变换** `课堂互动`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `基于基底变换的坐标变换`

**1. $[x]_U$ -> $[x]_V$表示的含义是( )。**  
 
A. 将坐标x从基底V迁移到基底U  
B. 将坐标x从基底U迁移到基底V    
C. 将向量U的x坐标分量迁移到向量V  
D. 将向量V的x坐标分量迁移到向量U

<br/>

**2. 一般情况下，下面哪个符号用于表示空间的标准基。**

A. $u$  
B. $v$  
C. $e$  
D. $a$


<br/>

**3. 令 $u=(4,3)^𝑇，v=(-1,2)^𝑇$，若存在向量$x=3u-v$，则向量$x$的坐标为（ ）。**

A. $[[3*4+(-1)*(-1), 3*3+(-1)*2]] = [[13,7]]$  
B. $[[3*4+(-1)*(-1)], [3*3+(-1)*2]] = [[13],[7]]$  
C. $[[4*3, -1*3],[-1*3, 2*(-1)]] = [[12, -3],[-3, -2]]$  
D. $[[4*3, -1*3],[-1*3, 2*(-1)]] = [[12, -3],[-3, -2]]$

<br/>

## **【课堂互动二】** `从矩阵乘法的角度理解基底变换`

**1. 给定一个矩阵$A=\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$，若以A的列向量组为基的空间中存在向量$u=[6,8]^T$。则向量$u$在标准基和以矩阵$A$为基的空间中的坐标分别表示为：（ ）。**  

A. (6,8) (6,8)  
B. (6,8) (20,22)  
C. (20,22) (6,8)  
D. (20,22) (20,22)

<br/>

**2. 如果一个向量所存在的空间$R$的维度确定了，那么它就有一个固定的位置，这个位置就称为向量的坐标。无论其他量如何变化，该坐标值都不会变化。**

A. 对  
B. 错

<br/>

**3. 三阶方阵和三阶向量相乘将满足以下哪一个公式？**

A. $Au = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
=x\begin{bmatrix} a \\ d \\ g \end{bmatrix}
+y\begin{bmatrix} b \\ e \\ h \end{bmatrix}
+z\begin{bmatrix} c \\ f \\ i \end{bmatrix}$

B. $Au = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
=x\begin{bmatrix} a \\ b \\ c \end{bmatrix}
+y\begin{bmatrix} d \\ e \\ f \end{bmatrix}
+z\begin{bmatrix} g \\ h \\ i \end{bmatrix}$

<br/>

**4. 向量的空间位置由其所参考的基底和相对于基底的位置决定，简单说，向量的空间位置可以表示为基底乘以对应的坐标。**

A. 对  
B. 错

<br/>


**5. 给定一组向量$U=(\begin{bmatrix} a \\ c \end{bmatrix}, \begin{bmatrix} b \\ d \end{bmatrix})$, 及以该向量组A为基底的坐标$c(x,y)$。问，如果将该坐标迁移到以标准基为基底的空间后，新坐标为( )。**  

A. (x, y)  
B. (ax+bx, cy+dy)  
C. (ax+by, cx+dy)  
D. (ay+by, cx+dx) 

<br/>

## **【课堂互动三】** `从标准基开始的基底变换`

**1. 给定基底V和基于基底V的坐标c，我们可以得到该坐标在标准基下的坐标x为( )。**  

A. x=Uc  
B. x=cU  
C. x=U/c  
D. x=c/U 

<br/>

**2. 令$u_1=(1,-1)^T,u_2=(2,2)^T$。则坐标$x=(1,2)^T$相应于$[u_1,u_2]$的坐标向量为（ ）。**

A. $\begin{bmatrix} 1 & 2 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix}$  
B. $\begin{bmatrix} 1 \\ 2 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ -1 & 2 \end{bmatrix}$  
C. $\begin{bmatrix} 1 & 2 \\ -1 & 2 \end{bmatrix}^{-1} \begin{bmatrix} 1 \\ 2 \end{bmatrix}$  
D. $\begin{bmatrix} 1 \\ 2 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ -1 & 2 \end{bmatrix}^{-1}$


## **【课堂互动四】** `从任意基开始的基底变换`

**1. 从$[v_1,v_2]$到$[u_1,u_2]$的转换可以看成是一个两步的过程。首先从$[v_1,v_2]$转换为标准基$[e_1,e_2]$，然后再从标准基转换为$[u_1,u_2]$。那么如果给定基于$V$的坐标$w$，我们可以得到基于$U$的坐标$x$的求解公式为：（ ）。**

A. $x=UVw$  
B. $x=UV^{-1}w$  
C. $x=U^{-1}Vw$  
D. $x=U^{-1}V^{-1}w$

<br/>

**2. 下列用于求解矩阵A的逆矩阵B的Python代码，正确的一个是（ )。**

A. B = np.inv(A)  
B. B = scipy.inv(A)   
C. B = linalg.inv(A)  
D. B = np.dot(A)


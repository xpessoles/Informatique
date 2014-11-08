// La fonction f renvoie 
function [val]=f(u,x0,x1,x2)
  val=(1-u)**2*x0+2*u*(1-u)*x1+u**2*x2;
endfunction

//printf("%f",f(0.5,0,1,2))

//global x0 x1 x2
//x0=0;x1=1;x2=2;
//function [val]=f(u)
//  val=(1-u)**2*x0+2*u*(1-u)*x1+u**2*x2;
//endfunction

//printf("%f",f(0.5))

function [res]=factorielle(n)
  if n==0
    res =1;
  else
    i=1;
    res=1;
    while i<=n
      res = res*i
      i=i+1
    end
  end  
endfunction

x0=0;y0=0;
x1=10;y1=10;
x2=20;y2=0;
n=50;
//x=[];y=[];
for i=1:n
  u=i/n;
 // printf("%f\n",u)
  x(i)=f(u,x0,x1,x2);
  y(i)=f(u,y0,y1,y2);
end

//plot2d(x,y)


inc = 0.1; i = 1;
u=0;
xx = []; yy = [];
while u<=1
    xx(i)=f(u,x0,x1,x2);
    yy(i)=f(u,y0,y1,y2);
    u=u+inc;
    i=i+1;
end
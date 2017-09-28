#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <vector>

double pi=3.14159;
double error=0.00001;

double next(double a, double b, double q0, double q1) {
	// std::cout<<"q0 = "<<q0<<"  q1 = "<<q1<<std::endl;
	double t0=q0*pi/180, t1=q1*pi/180;
	double m1 = b*(sin(t1)-sin(t0))/(a*(cos(t1)-cos(t0)));
	// std::cout<<"m1 = "<<m1<<std::endl;
	double th1 = atan(m1);
	// std::cout<<"theta1 = "<<th1*180/pi<<std::endl;
	double thm = atan((-b)*cos(t1)/(a*sin(t1)));
	// std::cout<<"thetaM = "<<thm*180/pi<<std::endl;
	double m2 = -tan(th1-2*thm);
	// std::cout<<"m2 = "<<m2<<std::endl;
	double x0=a*cos(t1),y0=b*sin(t1);
	// std::cout<<"x0 = "<<x0<<"  "<<"y0 = "<<y0<<std::endl;
	double X,Y;
	// std::cout<<std::endl;

	double alpha=y0-m2*x0;
	double gamma=b*b+a*a*m2*m2;
	double delta=2*a*a*m2*alpha;
	double epsilon=a*a*alpha*alpha-a*a*b*b;

	double r1=((-delta)+sqrt(delta*delta-4*gamma*epsilon))/(2*gamma);
	double r2=((-delta)-sqrt(delta*delta-4*gamma*epsilon))/(2*gamma);
	// std::cout<<"r1 = "<<r1<<"  r2 = "<<r2<<std::endl;
	X=(fabs(x0-r1)<=error)?(r2):(r1);
	// std::cout<<v.size()<<std::endl;

	alpha=1/m2;
	double beta=x0-y0/m2;
	gamma=a*a+alpha*alpha*b*b;
	delta=2*alpha*beta*b*b;
	epsilon=b*b*(beta*beta-a*a);

	r1=((-delta)+sqrt(delta*delta-4*gamma*epsilon))/(2*gamma);
	r2=((-delta)-sqrt(delta*delta-4*gamma*epsilon))/(2*gamma);
	// std::cout<<"r1 = "<<r1<<"  r2 = "<<r2<<std::endl;
	Y=(fabs(y0-r1)<=error)?(r2):(r1);

	// Y.push_back(180*asin(r1/b)/pi);
	// Y.push_back(180*asin(r2/b)/pi);
	double t;
	// std::cout<<a<<"  "<<b<<"  "<<X<<"  "<<Y<<"  "<<X/a<<"  "<<acos((X/a>1)?(1):(X/a))<<std::endl;	
	if(X/a>1)
		t=0;

	else if(X/a<-1)
		t=pi;

	else if(Y/b>1)
		t=pi/2;

	else if(Y/b<-1)
		t=3*pi/2;

	else if(fabs(X/a)<=error){
		// std::cout<<"LIENORDNI"<<std::endl;
		t=(Y/b>0)?(pi/2):(3*pi/2);
		// if(Y/b>0)
			// std::cout<<"+y axis"<<std::endl;
		// else
			// std::cout<<"-y axis"<<std::endl;
	}
	
	else if(X/a>0){
		// std::cout<<"LIENORDNI"<<std::endl;

		if(fabs(Y/b)<=error){
			t=0;
			// std::cout<<"+x axis"<<std::endl;
		}
		else if(Y/b>0) {
			t=acos(X/a);
			// std::cout<<"1st Quadrant"<<std::endl;
		}
		else {
			t=2*pi-acos(X/a);
			// std::cout<<"4th Quadrant"<<std::endl;
		}
	}

	else {
		// std::cout<<"LIENORDNI"<<std::endl;
		if(fabs(Y/b)<=error) {
			t=pi;
			// std::cout<<"-x axis"<<std::endl;			
		}
		else if(Y/b>0) {
			t=pi-asin(Y/b);
			// std::cout<<"2nd Quadrant"<<std::endl;
		}
		else {
			t=pi+acos(-X/a);
			// std::cout<<"3rd Quadrant"<<std::endl;
		}
	}

	return t*180/pi;
	// std::cout<<t*180/pi<<std::endl;
}

int main(int argc, char *argv[]){
	// std::cout<<next(5,10,90,-73)<<std::endl;
	// return 0;
	double x,y,z;
	double width=0.01;
	double a=5,b=10;
	double low=(180/pi)*acos(width/(2*a)),high=(180/pi)*acos(-width/(2*a));
	// std::cout<<low<<"  "<<high<<std::endl;
	// return 0;
	// 89.8855  90.1147

	x=90;
	y=(180/pi)*asin(-0.96);
	y=270;
	int i=0;
	while(true) {
		z=next(5,10,x,y);
		i++;
		if((z<=high && z>=low) || 0) {
			std::cout<<i<<" : "<<z<<std::endl;
			std::cout<<"x = "<<5*cos(pi*z/180);
			std::cin.get();
		}
		x=y;
		y=z;
	}

}


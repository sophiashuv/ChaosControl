a = 1.4; b = 0.3;
iter = 100000;
% Parameters
p = a;
dp_grens = 0.15;
fp = max(roots([a (1-b) -1])) % Theoretical fixed point
% Linearize:
A = [-2*a*fp , 1;
b , 0];
B = [0 ; fp];
lam = eig(A); % Eigenvalues of A
% Setting unstable eigenvalues to zero
i = 1;
while i <= length(lam);
if abs(lam(i)) >= 1
k(i) = 0; i=i+1;
else k(i) = lam(i); i=i+1;
End
End
% Pole placement
C = ctrb(A,B);
if size(B,1) == rank(C) % Controllability demand
K = acker(A,B,k);
K = K';
else error("Matrices A and B are not controllable!")
End
% Application to 1000 iterations
Xfp = [fp;b*fp]
X = [0;0]; % Initial condition
regelstap = [0];
a = p;
for i = 1:1000;
dp = -K'*(X(:,i)-Xfp);
if abs(dp) <= dp_grens
a = p + dp;
regelstap = [regelstap , dp];
else dp = 0; a = p + dp;
regelstap = [regelstap , dp];
End
X(1,i+1) = X(2,i)+1-a*X(1,i)^2;
X(2,i+1) = b*X(1,i);
End
tijd_X = 0:(length(X)-1);
% Visualization
figure(1)
subplot(2,1,1)
hold on, grid
plot(tijd_X,X(1,:),'-','MarkerSize',5)
ylabel('Response x','FontSize',15)
subplot(2,1,2)
hold on, grid
plot(tijd_X,regelstap,'r-','MarkerSize',5)
xlabel('timestep','FontSize',15),
ylabel('Control effort \deltaa','FontSize',15);
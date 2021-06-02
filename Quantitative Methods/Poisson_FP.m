%Poisson distribution
    %Antonio Junco de Haas      - A01339695
    %Daniel Roa Gonzalez        - A01021960
    %Sergio Hernández Castillo  - A01025210
    %Sebastián Vives Faus       - A01025211
semesters = 9;      %total amount of semesters
failedSubjects = (sum([0 0 0 1 1 2 3 3 4])); %set of possible failed subjects per student

lambda = failedSubjects/semesters;
disp(lambda)

fails = 3:6;    %range of classes that a student can fail and be placed in Apoyo Academico

%{
p = poisspdf(fails, lambda);
disp(p)

 figure
bar(fails, p, 1);
xlabel('Failed classes');
ylabel('Probability'); 
%}

%{
 regFails = 1:2;
p0 = poisspdf(regFails, lambda);
disp(p0)

figure
bar(regFails, p0, 1);
%}

allClasses = 1:6;
pAll = poisspdf(allClasses, lambda);
disp(pAll)

figure
bar(allClasses, pAll, 1);
xlabel('Failed classes');
ylabel('Probability'); 
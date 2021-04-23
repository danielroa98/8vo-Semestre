%Bernoulli distribution
    %Antonio Junco de Haas      - A01339695
    %Daniel Roa Gonzalez        - A01021960
    %Sergio Hernández Castillo  - A01025210
    %Sebastián Vives Faus       - A01025211    

% References:
    %https://www.mathworks.com/help/stats/bernoulli-distribution.html

%Probability of succes for the models
p = 0.75;

%PDF
%Range to evaluate
pdfRange = 0:1;
n = 1;

x = 0.1;
yPDF = binopdf(pdfRange, n, p);

figure
bar(x, yPDF, n);
xlabel('Observation');
ylabel('Probability');

%CDF
%Range to evaluate
cdfRange = -1:2;
yCDF = binocdf(cdfRange, 1, p);

figure
stairs(cdfRange, yCDF);
xlabel('Observation');
ylabel('Cumulative Probability');
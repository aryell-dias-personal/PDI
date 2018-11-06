clear all
close all
clc

%% leitura da imagem

Original = imread('Agucar_(2).jpg'); % transforma a imagem em matriz
mask = zeros(size(Original,1),size(Original,2)); % cria um matriz de mesmo tamanho da imagem

imshow(Original) %exibe a imagem original sem tratamento
title('Original')
figure

%% etapa de Sobel

kernel = [-1 -2 -1; 0 0 0; 1 2 1]; %masrcara de Sobel utilizada 

for x=1:size(Original,1) % loop para cobrir todas as linhas da matriz
    for y=1:size(Original,2) % loop para cobrir todas as colunas da matriz
        for i=-1:1 % loop pra percorrer as linhas do kernel
            for j=-1:1 %loop pra percorrer as colunas do kernel
                if (x + i > 0) && (x + i < size(Original,1)+1) && (y + j > 0) && (y + j < size(Original,2)+1) % condição para evitar pixels não existentes
                    mask(x,y) = mask(x,y) + double(Original(x+i,y+j))*kernel(2+i,2+j) + double(Original(x+i,y+j))*kernel(2+i,2+j)';
                    % calculo do valor do pixel central utilizando os dois
                    % kerneis de Sobel
                end
            end            
        end
    end
end

mask = uint8(mask); % mascara gerada pelo filtro

max = 0;
min = 300;

% etapa de normalização

for x=1:size(Original,1)
    for y=1:size(Original,2)
        if mask(x,y) < min
            min = mask(x,y);
        end
        if mask(x,y) > max
            max = mask(x,y);
        end
    end
end

mask = mask - min;
nor = 255/(max-min);

for x=1:size(Original,1)
    for y=1:size(Original,2)
        mask(x,y) = mask(x,y)*nor;
    end
end

imshow(mask) %exibe a mascara de Sobel
title('Sobel mask')
figure
SobelImg = Original;

for x=1:size(Original,1) % calculo da imagem filtrada por Sobel
    for y=1:size(Original,2)
        SobelImg(x,y) = double(Original(x,y)) - double(mask(x,y));
    end
end

% filtro de média para suavizar certas caracteristicas
media = 0;

for x=1:size(Original,1)
    for y=1:size(Original,2)
        for i=-1:1
            for j=-1:1
                if (x+i>0) && (x+i<=size(Original,1)) && (y+j>0) && (y+j<=size(Original,2))
                    media = media + double(SobelImg(x+i,y+j));
                end
            end
        end
        SobelImg(x,y) = uint8(media/9);
        media = 0;
    end
end

imshow(SobelImg) %exibe imagem final da etapa de Sobel
title('Sobel Img')
figure

%% etapa de filtro Laplaciano

Lmask = zeros(size(Original,1),size(Original,2));
Lkernel = [1 1 1; 1 -8 1; 1 1 1]; % kernel de laplace utilizado 

for x=1:size(Original,1)
    for y=1:size(Original,2)
        for i=-1:1
            for j=-1:1
                if (x + i > 0) && (x + i < size(Original,1)+1) && (y + j > 0) && (y + j < size(Original,2)+1)
                    Lmask(x,y) = Lmask(x,y) + double(Original(x+i,y+j))*Lkernel(2+i,2+j);
                    %cria a mascara de Laplace
                end
            end
        end
    end
end

LaplacianImg = Original - uint8(Lmask); % calcula a imagem de Laplace resultante

imshow(LaplacianImg)
title('Laplacian Img')
figure

%% finalização da filtragem

Result = (double(LaplacianImg)).*(double(SobelImg)); % calculo para gerar a imagem resultante dos dois filtros

% normalização

max = 0;
min = 300;

for x=1:size(Original,1)
    for y=1:size(Original,2)
        if Result(x,y) < min
            min = Result(x,y);
        end
        if Result(x,y) > max
            max = Result(x,y);
        end
    end
end

Result = Result - min;
nor = 255/(max-min);

for x=1:size(Original,1)
    for y=1:size(Original,2)
        Result(x,y) = Result(x,y)*nor;
    end
end

Result = uint8(Result);

imshow(Result) % exibe a imagem final
title('Result')

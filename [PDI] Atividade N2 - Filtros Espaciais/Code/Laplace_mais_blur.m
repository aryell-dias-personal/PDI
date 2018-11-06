clear all
close all
clc

%% leitura da imagem

Original = imread('Agucar_(2).jpg'); % transforma a imagem em matriz
Lmask = zeros(size(Original,1),size(Original,2)); % cria um matriz de mesmo tamanho da imagem

imshow(Original) %exibe a imagem original sem tratamento
title('Original')
figure

%% etapa para filtro de laplace

Lkernel = [1 1 1; 1 -8 1; 1 1 1]; % kernel de Laplace

for x=1:size(Original,1)
    for y=1:size(Original,2)
        for i=-1:1
            for j=-1:1
                if (x + i > 0) && (x + i < size(Original,1)+1) && (y + j > 0) && (y + j < size(Original,2)+1)
                    Lmask(x,y) = Lmask(x,y) + double(Original(x+i,y+j))*Lkernel(2+i,2+j);
                end
            end
        end
    end
end

LaplacianImg = Original - uint8(Lmask); % calculo da imagem após o filtro de Laplace

%% etapa unsharp masking e highboost filteriing

Blur = zeros(size(Original,1),size(Original,2));

% filtro de média

media = 0;

for x=1:size(Original,1)
    for y=1:size(Original,2)
        for i=-4:4
            for j=-4:4
                if (x+i>0) && (x+i<=size(Original,1)) && (y+j>0) && (y+j<=size(Original,2))
                    media = media + double(LaplacianImg(x+i,y+j));
                end
            end
        end
        Blur(x,y) = uint8(media/81);
        media = 0;
    end
end

Blur = LaplacianImg - uint8(Blur); %calculo da imagem borrada

imshow(Blur) % exibe imagem borrada
title('Blur Img')
figure

k=0.8;

LaplacianImg = LaplacianImg + k*Blur; %calculo da imagem após adição de parte da imagem borrada

% filtro de média pra diminuir ruidoos

media = 0;

for x=1:size(Original,1)
    for y=1:size(Original,2)
        for i=-1:1
            for j=-1:1
                if (x+i>0) && (x+i<=size(Original,1)) && (y+j>0) && (y+j<=size(Original,2))
                    media = media + double(LaplacianImg(x+i,y+j));
                end
            end
        end
        Blur(x,y) = uint8(media/9);
        media = 0;
    end
end

imshow(LaplacianImg) % exibe imagem final
title('Laplacian Img')
%}


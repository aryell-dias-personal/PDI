clear all
close all
clc

%% leitura da imagem

Original = imread('Agucar_(1).jpg'); % transforma a imagem em matriz
mask = zeros(size(Original,1),size(Original,2)); % cria um matriz de mesmo tamanho da imagem

imshow(Original) %exibe a imagem original sem tratamento
title('Original')
figure

%% etapa unsharp masking e highboost filteriing

media = 0; %filtro de média

for x=1:size(Original,1)
    for y=1:size(Original,2)
        for i=-3:3
            for j=-3:3
                if (x+i>0) && (x+i<=size(Original,1)) && (y+j>0) && (y+j<=size(Original,2))
                    media = media + double(Original(x+i,y+j));
                end
            end
        end
        mask(x,y) = uint8(media/81);
        media = 0;
    end
end

mask = Original - uint8(mask); % imagem filtrada

imshow(mask) % exibe imagem filtrada
figure

% utiliza função de potência para clarear a imagem

for x=1:size(Original,1)
    for y=1:size(Original,2)
        mask(x,y) = 2*double(mask(x,y))^0.9;
    end
end

result = uint8(mask);

imshow(result) % exibe imagem final

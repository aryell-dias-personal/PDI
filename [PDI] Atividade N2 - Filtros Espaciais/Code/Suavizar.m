clear all
close all
clc

%% leitura da imagem

Original = imread('Suavizar_(2).jpg');
mask = zeros(size(Original,1),size(Original,2));
imshow(Original)
title('original')
figure

media = 0;
std = 0;

for x=1:size(Original,1)
    for y=1:size(Original,2)
        for i=-7:7
            for j=-7:7
                if (x + i > 0) && (x + i < size(Original,1)+1) && (y + j > 0) && (y + j < size(Original,2)+1) 
                    media = media + double(Original(x+i,y+j)/225);
                end
            end
        end
        for i=-7:7
            for j=-7:7
                if (x + i > 0) && (x + i < size(Original,1)+1) && (y + j > 0) && (y + j < size(Original,2)+1) 
                    std = std + sqrt((double(Original(x+i,y+j)) - media)^2)/15;
                end
            end
        end
        media = 49;
        mediana = zeros(7,7);
        if (std > 10)
            med = 0;
            for i=-3:3
                for j=-3:3
                    if (x + i > 0) && (x + i < size(Original,1)+1) && (y + j > 0) && (y + j < size(Original,2)+1) 
                        mediana(4+i,4+j) = Original(x+
                    end
                end
            end
            mask(x,y) = med/49;
        end
        std = 0;
    end
end

mask = uint8(mask);

imshow(mask)
title('mask')

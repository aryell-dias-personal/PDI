function [zoom_in] = zoom(imagem,y,x)

%clear all;
%clc;

Zoom = imread(imagem); % ler a imagem a ser usada
zoomed = uint8(zeros(x,y)); % cria uma imagem do tamanho desejado

r = 1; %variável auxiliar para o no. de linhas da imagem com zoom
c = 1; %variável auxiliar para o no. de colunas da imagem com zoom

for y=1:size(Zoom,2) % loop para expandir a imagem o máximo possível
    for x=1:size(Zoom,1) % utilizando no. inteiros
        for i=0:(floor(size(zoomed,1)/size(Zoom,1))-1)  
            for j=0:(floor(size(zoomed,2))/size(Zoom,2)-1)
                zoomed(r+i,c+j) = Zoom(x,y);
            end
        end
        r = r + floor(size(zoomed,1)/size(Zoom,1));
    end
    r = 1;
    c = c + floor(size(zoomed,2)/size(Zoom,2));
end

aux1 = zoomed; %imagem auxiliar 

for y=1:size(zoomed,2) %loop para adicionar as linhas extras ao longo da imagem
    j = 1;
    h = floor(floor(size(zoomed,1)/size(Zoom,1))*size(Zoom,1)/(size(zoomed,1) - floor(size(zoomed,1)/size(Zoom,1))*size(Zoom,1)));
    for x=1:h+1:size(zoomed,1)
        t=size(zoomed,1)-x;
        aux1(x,y) = 0;
        for i = 1:t
            aux1(x+i,y) = zoomed(x+i-j,y);
        end
        j=j+1;
    end        
end

aux2 = aux1;

for x=1:size(zoomed,1) %loop para adicionar as colunas extras ao longo da imagem
    j = 1;
    h = floor(floor(size(zoomed,2)/size(Zoom,2))*size(Zoom,2)/(size(zoomed,2) - floor(size(zoomed,2)/size(Zoom,2))*size(Zoom,2)));
    for y=1:h+1:size(zoomed,2)
        t=size(zoomed,2)-y;
        aux1(x,y) = 0;
        for i = 1:t
            aux1(x,y+i) = aux2(x,y+i-j);
        end
        j=j+1;
    end        
end


for x=1:size(zoomed,1) % interpola os valores dos pixels pretos com os 
    for y=1:size(zoomed,2) % valores da vizinhança (N8)
        valor = 0;
        total = 0;
        if aux1(x,y) == 0
            for i=-1:1
                for j=-1:1
                    if (x+i > 0) && (x+i < (size(zoomed,1)+1)) && (y+j > 0) && (y+j < (size(zoomed,2)+1))
                        if aux1(x+i,y+j) ~= 0
                            valor = valor + double(aux1(x+i,y+j));
                            total = total + 1;
                        end
                        
                    end
                end
            end
            aux1(x,y) = uint8(round(valor/total));
        end
    end
end

imshow(aux1)
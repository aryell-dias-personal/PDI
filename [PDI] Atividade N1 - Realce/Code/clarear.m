function [clarear] = clarea(imagem)

Imagem = imread(imagem);
clarea = Imagem;

med = mean(Imagem);
aux = 0;
for i=1:length(med)
    if med(i) > aux
        aux = med(i);
    end
end

max = 0;
min = 300;

for x=1:size(Imagem,1)
    for y=1:size(Imagem,2)
        clarea(x,y) = aux*log(double(Imagem(x,y)+1));
        if clarea(x,y) > max
            max = clarea(x,y);
        end
        if clarea(x,y) < min
            min = clarea(x,y);
        end
    end
end

t = 255/max;

for x=1:size(clarea,1)
    for y=1:size(clarea,2)
        clarea(x,y) = uint8((double(clarea(x,y)) - min)*t);
    end
end
        
imshow(clarea)
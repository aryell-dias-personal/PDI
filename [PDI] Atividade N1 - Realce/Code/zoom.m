%function zoom_in = zoom(imagem)

clear all;
clc;

Zoom = imread('Zoom_in_(1).jpg');
zoomed = uint8(zeros(480,360));

r = 1;
c = 1;

for y=1:100
    for x=1:150
        for i=0:2  
            for j=0:2
                zoomed(r+i,c+j) = Zoom(x,y);
            end
        end
        r = r + 3;
    end
    r = 1;
    c = c + 3;
end

aux1 = zoomed;

for y=1:360
    j = 1;
    for x=1:16:480
        t=480-x;
        aux1(x,y) = 0;
        for i = 1:t
            aux1(x+i,y) = zoomed(x+i-j,y);
        end
        j=j+1;
    end        
end

aux2 = aux1;

for x=1:480
    j = 1;
    for y=1:6:360
        t=360-y;
        aux1(x,y) = 0;
        for i = 1:t
            aux1(x,y+i) = aux2(x,y+i-j);
        end
        j=j+1;
    end        
end


for x=1:480
    for y=1:360
        valor = 0;
        total = 0;
        if aux1(x,y) == 0
            for i=-1:1
                for j=-1:1
                    if (x+i > 0) && (x+i < 481) && (y+j > 0) && (y+j < 361)
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
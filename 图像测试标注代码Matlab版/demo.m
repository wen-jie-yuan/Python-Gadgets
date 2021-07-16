% ͼ����Ա�ע���룬��ע�Ŵ�����Ϊ���·�

clc;
clear;
% ��ȡͼ��·������Ҫ����׺
im_src = double(imread('image_path'));
[height, width, channel1] = size(im_src);

% ���忪ʼ����㣬��ѡ��Сrect_size���Ŵ�����m_factor
[start_y, start_x] = deal(40, 40);
rect_size = 60;
m_factor = 2;

% �ü��Ŵ�
tt = im_src(start_y:start_y+rect_size-1, start_x:start_x+rect_size-1, :);
tt_big = imresize(tt,m_factor);
[m_height, m_width, channel2]=size(tt_big);

% ����ѡͼ�������ԭͼ���·�
if channel1 == 3
    for i=1:3
        im_src(1+height-rect_size*m_factor:height, width-m_width+1:width, i)=tt_big(:,:,i);
    end
else
    im_src(1+height-rect_size*m_factor:height, width-m_width+1:width)=tt_big;
end

% ���ƿ��� 
s=draw_rect(im_src, [start_y,start_x],[rect_size, rect_size], 3, [255, 0, 0]);
result=draw_rect(s, [height-m_height, width-m_width],[m_height, m_width], 3, [255, 0, 0]);

imshow(uint8(result));
imwrite(uint8(result), 'output.png');
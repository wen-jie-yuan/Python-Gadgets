import cv2
from skimage.metrics import mean_squared_error,peak_signal_noise_ratio
from skimage.measure import compare_ssim

img1 = cv2.imread('image1.png')
img2 = cv2.imread('image2.png')
MSE = mean_squared_error(img1, img2)
PSNR = peak_signal_noise_ratio(img1, img2)
SSIM = compare_ssim(img1, img2, multichannel=True)
print('MSE: ', MSE)
print('PSNR: ', PSNR)
print('SSIM: ', SSIM)

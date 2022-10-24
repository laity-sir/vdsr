import torch
import matplotlib.pyplot as plt

hh=torch.load('./save_data.pth',map_location=lambda storage, loc: storage)
print(hh)
train_loss=[]
test_loss=[]
test_psnr=[]
test_ssim=[]
for i in sorted(hh):
    print(i)
    train_loss.append(hh[i]['train_loss'])
    test_psnr.append(hh[i]['test_psnr'])

print(train_loss)
# plt.plot(train_loss,label='train_loss')

plt.plot(test_psnr,label='test_psnr')

plt.legend(loc='upper right')
plt.title('loss')

plt.savefig('./psnr.png')
plt.show()
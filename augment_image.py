import argparse
import os
import PIL.Image as pil_image

def augment_img(args):
    if not os.path.exists('./train'):
        os.makedirs('./train')
    count=1
    for i, image_path in enumerate(sorted(os.listdir(args.images_dir))):
        basename = image_path.split('/')[-1]
        basename = basename.split('.')[0]  ###baby
        hr = pil_image.open(os.path.join(args.images_dir,image_path)).convert('RGB')
        for r in [0,90,180,270]:
            for s in [0,1]:
                tmp=hr.rotate(r,expand=True)
                if s==1:
                    tmp=tmp.transpose(pil_image.FLIP_TOP_BOTTOM)
                elif s==2:
                    tmp=tmp.transpose(pil_image.FLIP_LEFT_RIGHT)
                else:
                    tmp=tmp
                count+=1
                tmp.save(os.path.join('./train', '{}_{}.png'.format(basename,count)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--images-dir', type=str, default='./291')
    args = parser.parse_args()
    augment_img(args)
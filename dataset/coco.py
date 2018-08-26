# -----------------------------------------------------------------------
# HashGAN: Deep Learning to Hash with Pair Conditional Wasserstein GAN
# Licensed under The MIT License [see LICENSE for details]
# Modified by Bin Liu
# -----------------------------------------------------------------------


from .dataset import data_generator


def load(batch_size, width_height):
    return (
        data_generator(batch_size, width_height, "../data_list/coco/train.txt"),
        data_generator(batch_size, width_height, "../data_list/coco/database_nolabel.txt"),
        data_generator(batch_size, width_height, "../data_list/coco/test.txt")
    )


def load_val(batch_size, width_height):
    return (
        data_generator(batch_size, width_height, "../data_list/coco/database.txt"),
        data_generator(batch_size, width_height, "../data_list/coco/test.txt")
    )


if __name__ == "__main__":
    gens = load(4, "")
    for gen in gens:
        data, label = next(gen())
        print(data)
        print(label)

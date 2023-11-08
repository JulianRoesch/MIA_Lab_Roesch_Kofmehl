"""The pre-processing module contains classes for image pre-processing.

Image pre-processing aims to improve the image quality (image intensities) for subsequent pipeline steps.
"""
import warnings

import pymia.filtering.filter as pymia_fltr
import SimpleITK as sitk
import numpy as np

class ImageNormalization(pymia_fltr.Filter):
    """Represents a normalization filter."""

    def __init__(self):
        """Initializes a new instance of the ImageNormalization class."""
        super().__init__()

    def execute(self, image: sitk.Image, params: pymia_fltr.FilterParams = None) -> sitk.Image:
        """Executes a normalization on an image.

        Args:
            image (sitk.Image): The image.
            params (FilterParams): The parameters (unused).

        Returns:
            sitk.Image: The normalized image.
        """

        img_arr = sitk.GetArrayFromImage(image)

        # todo: normalize the image using numpy
        #warnings.warn('No normalization implemented. Returning unprocessed image.')

        #max_val = img_arr.max()
        #min_val = img_arr.min()
        #new_min_val = 0
        #new_max_val = 255
        #new_diff = new_max_val - new_min_val

        #rescaled_img_arr = np.round(((img_arr - min_val) / (max_val - min_val) * new_diff) + new_min_val)

        # Z-score standardization
        mean = np.mean(img_arr)
        std_dev = np.std(img_arr)
        standardized_data = (img_arr - mean) / std_dev


        img_out = sitk.GetImageFromArray(standardized_data)
        img_out.CopyInformation(image)

        return img_out

    def __str__(self):
        """Gets a printable string representation.

        Returns:
            str: String representation.
        """
        return 'ImageNormalization:\n' \
            .format(self=self)


class SkullStrippingParameters(pymia_fltr.FilterParams):
    """Skull-stripping parameters."""

    def __init__(self, img_mask: sitk.Image):
        """Initializes a new instance of the SkullStrippingParameters

        Args:
            img_mask (sitk.Image): The brain mask image.
        """
        self.img_mask = img_mask


class SkullStripping(pymia_fltr.Filter):
    """Represents a skull-stripping filter."""

    def __init__(self):
        """Initializes a new instance of the SkullStripping class."""
        super().__init__()

    def execute(self, image: sitk.Image, params: SkullStrippingParameters = None) -> sitk.Image:
        """Executes a skull stripping on an image.

        Args:
            image (sitk.Image): The image.
            params (SkullStrippingParameters): The parameters with the brain mask.

        Returns:
            masked_img (sitk.Image:) The masked image.
        """

        # remove the skull from the image by using the brain mask
        # Mask input image with binary mask
        img_arr = sitk.GetArrayFromImage(image)
        mask = params.img_mask  # the brain mask
        mask_arr = sitk.GetArrayFromImage(mask)

        img_arr[mask_arr == 0] = 0



        image_return = sitk.GetImageFromArray(img_arr)

        return image_return

    def __str__(self):
        """Gets a printable string representation.

        Returns:
            str: String representation.
        """
        return 'SkullStripping:\n' \
            .format(self=self)


class ImageRegistrationParameters(pymia_fltr.FilterParams):
    """Image registration parameters."""

    def __init__(self, atlas: sitk.Image, transformation: sitk.Transform, is_ground_truth: bool = False):
        """Initializes a new instance of the ImageRegistrationParameters

        Args:
            atlas (sitk.Image): The atlas image.
            transformation (sitk.Transform): The transformation for registration.
            is_ground_truth (bool): Indicates weather the registration is performed on the ground truth or not.
        """
        self.atlas = atlas
        self.transformation = transformation
        self.is_ground_truth = is_ground_truth


class ImageRegistration(pymia_fltr.Filter):
    """Represents a registration filter."""

    def __init__(self):
        """Initializes a new instance of the ImageRegistration class."""
        super().__init__()

    def execute(self, image: sitk.Image, params: ImageRegistrationParameters = None) -> sitk.Image:
        """Registers an image.

        Args:
            image (sitk.Image): The image.
            params (ImageRegistrationParameters): The registration parameters.

        Returns:
            sitk.Image: The registered image.
        """

        # replace this filter by a registration. Registration can be costly, therefore, we provide you the
        # transformation, which you only need to apply to the image!
        #warnings.warn('No registration implemented. Returning unregistered image')

        atlas = params.atlas
        transform = params.transformation
        is_ground_truth = params.is_ground_truth  # the ground truth will be handled slightly different

        out = sitk.Resample(image, referenceImage=atlas, transform=transform, interpolator=sitk.sitkLinear,
                      defaultPixelValue=0.0, outputPixelType=image.GetPixelIDValue())



        return out

    def __str__(self):
        """Gets a printable string representation.

        Returns:
            str: String representation.
        """
        return 'ImageRegistration:\n' \
            .format(self=self)

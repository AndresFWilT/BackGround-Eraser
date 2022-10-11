from __future__ import annotations
from abc import ABC
from rembg import remove
from PIL import Image
import os

class BackgroundDeletion():
    # global
    __file_path = None
    __save_path = None
    __image = None
    __out_name = None
    __in_name = None
    """
    Class that deletes the background of an image, but returning the path of
    both images (the original one and the background deleted)
    """
    def __init__(self,image) -> None:
        """
        constructor
        """
        self.image = image

    def save_image(self):
        """
        function that saves the uploaded image in to the file system
        and return it's input path
        """
        simp_path = "static/images/"+self.image
        self.file_path = os.path.abspath(simp_path)
        return self.file_path
    
    def delete_background(self,input_path):
        """
        function that removes the background of the image, and
        return de output path
        """
        input_name_w_extension,output_name = self.create_output_name(input_path)
        output_path = input_path.replace(input_name_w_extension,output_name)
        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)
        self.save_path = output_path
        return self.file_path,self.save_path

    def create_output_name(self,input):
        """
        function that creates the name of the erased image
        """
        splitted_string = input.split('\\')
        splitted_input_name = splitted_string[len(splitted_string)-1].split('.')
        self.in_name = splitted_string[len(splitted_string)-1]
        self.out_name = 'bckgnd-erased_'+splitted_input_name[0]+'.png'
        return splitted_string[len(splitted_string)-1],self.out_name

    def get_names(self):
        return self.in_name,self.out_name

    # getter / setter

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self,file_path):
        self.__file_path = file_path

    @property
    def save_path(self):
        return self.__save_path

    @save_path.setter
    def save_path(self,save_path):
        self.__save_path = save_path

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self,image):
        self.__image = image

    @property
    def out_name(self):
        return self.__out_name

    @out_name.setter
    def out_name(self,out_name):
        self.__out_name = out_name

    @property
    def in_name(self):
        return self.__in_name

    @in_name.setter
    def in_name(self,in_name):
        self.__in_name = in_name
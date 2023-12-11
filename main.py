import cv2
import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys
class SiftConfigurator:
    def __init__(self):
        self.sift = cv2.xfeatures2d.SIFT_create()

class MatcherConfigurator:
    def __init__(self):
        super().__init__()
        self.FLANN_INDEX_KDTREE = 0
        self.index_params = dict(algorithm=self.FLANN_INDEX_KDTREE, trees=5)
        self.search_params = dict(checks=80)

class ObjectDetector:
    def __init__(self):
        super().__init__()

    def detect_object(self, target, ref, Imagebase, result):
        keypts_base, descr_base = self.sift.detectAndCompute(Imagebase, None)
        keypts_obj, descr_obj = self.sift.detectAndCompute(ref["image"], None)

        flann = cv2.FlannBasedMatcher(self.index_params, self.search_params)
        matches = flann.knnMatch(descr_obj, descr_base, k=2)

        matches = [[i] for i, j in matches if i.distance < 0.83 * j.distance]

        bounding_box = None  # Variable to store the bounding box coordinates

        if len(matches) > 20:
            src_pts = np.float32([keypts_obj[m[0].queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([keypts_base[m[0].trainIdx].pt for m in matches]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            h, w, d = ref["image"].shape
            pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
            dst = np.int32(cv2.perspectiveTransform(pts, M))

            matching_top_point = tuple(dst[np.argmin([x[0][1] for x in dst])][0])
            result = cv2.polylines(result, [dst], True, (100, 250, 200), 1, cv2.LINE_AA)
            cv2.putText(result, ref["name"], matching_top_point, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255, 255, 255), 2)
            
            # Calculate bounding box coordinates
            bounding_box = cv2.boundingRect(np.int32(dst))

        else:
            print("Could not find any satisfying matches for {}".format(ref["name"]))
            return False, None

        matching_img = cv2.drawMatchesKnn(ref["image"], keypts_obj, Imagebase, keypts_base, matches, None, flags=2)

        plt.imshow(matching_img)
        plt.axis('off')  # Hide axes
        plt.show()

        return True, bounding_box

class ResultDisplayer:
    def display_result(self, result, target_name, name_insert):
        result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        plt.imshow(result_rgb)
        plt.title('Final result for {} (refs found: {})'.format(target_name, ", ".join(name_insert)))
        plt.axis('off')  # Hide axes
        plt.show()

def correct_file_type(file):
        accepted_file_ext=["jpg", "jpeg", "png"]

        x=file.split(".")
        if x[-1].lower() in accepted_file_ext:
            return True
        else:
            return False    
    

if __name__ == "__main__":
 #   try:
        print("Enter the number of images you want to use:")
        try:
            no_of_images = int(input())
            if no_of_images<1:
                raise ValueError
        
        except ValueError:
            print("This is not a valid number, exiting program...")
            sys.exit()
        print("Enter the image name")
        fileobject = []
        for i in range(no_of_images):
            x=False
            while not x:
                print("Enter the object %d image:" % (i + 1))
                img_path=input()
                if os.path.exists(img_path) & correct_file_type(img_path):
                    fileobject.append(img_path)
                    x=True
                else:
                    print("Invalid file type or incorrect file path, Please try again:")

                
        
        images_objects = []
        for i in range(no_of_images):
            images_objects.append(cv2.imread(fileobject[i]))

        print("Enter the base image:")
        filename_ref = input()
        
        Imagebase = cv2.imread(filename_ref)

        split = [i.split('.')[0] for i in fileobject]

        filename_object = [cv2.imread(file) for file in fileobject]
        target = {"name": filename_ref.split('.')[0], "image": Imagebase}
        refs = [{"name": name, "image": cv2.imread(file)} for name, file in zip(split, fileobject)]

        detector = ObjectDetector()
        result_displayer = ResultDisplayer()

        result = target["image"].copy()
        name_insert = []

        for ref in refs:
            success, bounding_box = detector.detect_object(target, ref, Imagebase, result)
            if success:
                name_insert.append(ref["name"])
                print(f"Bounding box coordinates for {ref['name']}: {bounding_box}")

        result_displayer.display_result(result, target["name"], name_insert)
  #  except Exception as err:
   #     print("Something was wrong with your image file. Please ensure you have the correct image and try again")
   #     exit()


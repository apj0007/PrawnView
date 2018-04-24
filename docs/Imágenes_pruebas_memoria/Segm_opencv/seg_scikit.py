def a(image): 
  import numpy as np
  import matplotlib.pyplot as plt
  from scipy import ndimage as ndi

  from skimage.morphology import watershed
  from skimage.feature import peak_local_max
  
  gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  ret, image = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)



  # Now we want to separate the two objects in image
  # Generate the markers as local maxima of the distance to the background
  distance = ndi.distance_transform_edt(image)
  local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
                              labels=image)
  markers = ndi.label(local_maxi)[0]
  labels = watershed(-distance, markers, mask=image)

  fig, axes = plt.subplots(ncols=3, figsize=(9, 3), sharex=True, sharey=True)
  ax = axes.ravel()

  ax[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
  ax[0].set_title('Overlapping objects')
  ax[1].imshow(-distance, cmap=plt.cm.gray, interpolation='nearest')
  ax[1].set_title('Distances')
  ax[2].imshow(labels, cmap=plt.cm.nipy_spectral, interpolation='nearest')
  ax[2].set_title('Separated objects')

  for a in ax:
      a.set_axis_off()

  fig.tight_layout()
  plt.show()

import numpy as np

# Array data
# N = 8  # number of radiating elements
# d = 0.5  # distance between adjacent antennas in wavelength units


def beamforming(N,d,theta_s)
# Define the array response function
  #theta_s = np.deg2rad(30)  # steering angle of the main lobe
  def array_response(theta):
      """
      Calculates the array response function for a linear array of antennas.

      Args:
          theta (numpy.ndarray): An array of angles of arrival in radians.

      Returns:
          numpy.ndarray: An array of complex numbers representing the response of
          each antenna in the array to an incoming signal from the given angles.
      """
      return np.exp(-1j * 2 * np.pi * d * np.outer(np.arange(N), np.sin(theta)))

  # Calculate the beamforming weights
  a = array_response(theta_s)
  w = a / np.linalg.norm(a)

  # Calculate the beamforming gain
  theta_scan = np.linspace(-np.pi/2, np.pi/2, 181)  # scan angles
  AF = np.abs(np.sum(array_response(theta_scan) * w, axis=1))
  BF_gain = 10 * np.log10(np.max(AF) / np.mean(AF))
return  BF_gain
# Print the beamforming gain
# print(f"Beamforming gain: {BF_gain:.2f} dB")

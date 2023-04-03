import numpy as np

def array_response(theta, d, N):
    """
    Calculates the array response function for a linear array of antennas.

    Args:
        theta (numpy.ndarray): An array of angles of arrival in radians.

    Returns:
        numpy.ndarray: An array of complex numbers representing the response of
        each antenna in the array to an incoming signal from the given angles.
    """
    return np.exp(-1j * 2 * np.pi * d * np.outer(np.arange(N), np.sin(theta)))

def bf_calculation(N, d, theta_deg):
    theta_s = np.deg2rad(theta_deg)  # steering angle of the main lobe

    # Define the array response function
    a = array_response(theta_s, d, N)

    # Calculate the beamforming weights
    w = a / np.linalg.norm(a)

    # Calculate the beamforming gain
    theta_scan = np.linspace(-np.pi/2, np.pi/2, 181)  # scan angles
    AF = np.abs(np.sum(array_response(theta_scan, d, N) * w, axis=1))
    BF_gain = 10 * np.log10(np.max(AF) / np.mean(AF))

    return BF_gain

import numpy as np

def dft2d(image):
    j = np.complex(0,1)
    N, M = image.shape
    x, y = np.meshgrid(range(M), range(N))
    result = []
    for v in range(N):
        result.append([])
        for u in range(M):
            complex_exp = np.exp(-j*2*np.pi*(u*x/M + v*y/N))
            result[v].append(np.sum(image*complex_exp))
        print('{} %'.format(100*v/(N-1)))
    return np.array(result)

def idft2d(image_transform):
    N, M = image_transform.shape
    result_conjugate = dft2d(np.conjugate(image_transform))/(M*N)
    return np.conjugate(result_conjugate)

def ifft2d(image_transform):
    N, M = image_transform.shape
    result_conjugate = fft2d(np.conjugate(image_transform))/(M*N)
    return np.conjugate(result_conjugate)

def fft(x):
    j = np.complex(0,1)
    N = len(x)
    if N == 1:
        return x
    x_even = x[::2]
    print(x_even)
    x_odd = x[1::2]

    F_even = fft(x_even)
    F_odd = fft(x_odd)

    u = np.array(range(N//2))
    complex_exp_odd = np.exp(-j*2*np.pi*u/N)*F_odd
    F_left = F_even + complex_exp_odd
    F_right = F_even - complex_exp_odd
    return np.concatenate([F_left, F_right])

def fft2d(image):
    aux = np.array([fft(line) for line in image])
    return np.array([fft(line) for line in aux.transpose()]).transpose()

def padImage(image, powOf2=True):
    N, M = image.shape
    P, Q = 2*M-1, 2*N-1
    if powOf2:
        P = int(2**np.ceil(np.log2(P)))
        Q = int(2**np.ceil(np.log2(Q)))
    result = np.zeros([Q, P])
    result[:N, :M] = image
    return result

def idealLPF(height, width, cutoff):
    x, y = np.meshgrid(range(width), range(height))
    distance = np.sqrt((x-width/2)**2+(y-height/2)**2)
    return np.array(distance <= cutoff, dtype=np.float)

def butterworthLPF(height, width, cutoff, order=1):
    x, y = np.meshgrid(range(width), range(height))
    distance = np.sqrt((x-width/2)**2+(y-height/2)**2)
    return 1/(1+(distance/cutoff)**(2*order))
    
def gaussianLPF(height, width, cutoff):
    x, y = np.meshgrid(range(width), range(height))
    distance = np.sqrt((x-width/2)**2+(y-height/2)**2)
    return np.exp(-0.5*(distance/cutoff)**2)

def idealHPF(height, width, cutoff):
    return 1-idealLPF(height, width, cutoff)

def butterworthHPF(height, width, cutoff, order=1):
    return 1-butterworthLPF(height, width, cutoff, order)
    
def gaussianHPF(height, width, cutoff):
    return 1-gaussianLPF(height, width, cutoff)

def laplacian(height, width):
    x, y = np.meshgrid(range(width), range(height))
    distance2 = (x-width/2)**2+(y-height/2)**2
    return -4*(np.pi**2)*distance2
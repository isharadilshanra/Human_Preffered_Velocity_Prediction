from setuptools import find_packages, setup

package_name = 'mini_project_kf'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ishara',
    maintainer_email='isharadilshanra11@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'preferred_velocity_prediction_kf = mini_project_kf.preferred_velocity_prediction_kf:main',
        ],
    },
)

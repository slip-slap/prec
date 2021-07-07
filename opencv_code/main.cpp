#include <opencv2/core.hpp>
#include <opencv2/core/types.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <math.h>

#define window_width 800
#define window_height 600


void MyLine(cv::Mat img, cv::Point start, cv::Point end);
int Drawing_Random_Lines(cv::Mat img, char* window_name, cv::RNG rng);
static cv::Scalar randomColor(cv::RNG& rng);
cv::Mat  ReadImage(const char* path, const cv::Rect ROI);

double f(int x, int y)
{
	int x_frequency = 7;
	int x_coeff_a  = 50;
	int x_coeff_b  = 80;
	int y_frequency = 2;
	int y_coeff_a  = 9;
	int y_coeff_b  = 12;
	return x_coeff_a * std::cos(x_frequency * x) + x_coeff_b * std::sin(x_frequency * x) +
		y_coeff_a * std::cos(y_frequency * y) + y_coeff_b * std::sin(y_frequency * y);
}


cv::Mat d2fourier(){
	cv::Mat a(400, 400, CV_8UC3, cv::Scalar(0,0,255));

	for(int i = 0; i < 400; i++)
	{
		for(int k = 0; k < 400; k++)
		{
			int color = (int)f(i,k);
			cv::Mat one(1, 1, CV_8UC3, cv::Scalar(0,0,color));
			cv::Rect pos(i,k, 1, 1);
			one.copyTo(a(pos));
			std::cout<<one<<std::endl;
		}
	}
	std::cout<<CV_8UC3<<std::endl;

	return a;
}

int main()
{

	char title[] = "drawing line";
	
	cv::Mat image = cv::Mat::zeros(window_height, window_width,CV_8UC3);
	cv::RNG rng(0xFFFFFF);

	cv::Rect ROI(20,20,80,8);
	cv::Mat img = ReadImage("../lena.jpg",ROI);
	std::cout<<img<<std::endl;

	img.copyTo(image(ROI));
	cv::Rect fourier_ROI(100,100, 400, 400);
	cv::Mat fourier_image = d2fourier();
	fourier_image.copyTo(image(fourier_ROI));
	cv::imshow(title, image);
	cv::moveWindow(title,300, 50);

	while(true)
	{
		int key = cv::waitKey(1); 
		if(key == 'q')
			break;
	}
	return 0;
}


cv::Mat ReadImage(const char* path, const cv::Rect ROI)
{
	cv::Mat image = cv::imread(path, cv::IMREAD_COLOR);
	cv::Mat after_resize_image;
	cv::resize(image,after_resize_image,cv::Size(ROI.width,ROI.height));
	return after_resize_image;
}

		//pt1.y = rng.uniform(0, window_height );
		//cv::line(img, pt1, pt2, randomColor(rng),rng.uniform(1,10),8);


static cv::Scalar randomColor(cv::RNG& rng)
{
	int icolor = (unsigned) rng;
	return cv::Scalar(icolor&255,(icolor>>8)&255,(icolor>>16)&255);
}

void MyLine(cv::Mat img, cv::Point start, cv::Point end)
{
	int thickness = 2;
	int line_Type = cv::LINE_8;
	cv::line(img, start, end, cv::Scalar(0,0,255),thickness, line_Type);
}




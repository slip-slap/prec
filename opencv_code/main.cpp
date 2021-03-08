#include <opencv2/core.hpp>
#include <opencv2/core/types.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

#define window_width 800
#define window_height 600


void MyLine(cv::Mat img, cv::Point start, cv::Point end);
int Drawing_Random_Lines(cv::Mat img, char* window_name, cv::RNG rng);
static cv::Scalar randomColor(cv::RNG& rng);
cv::Mat  ReadImage(const char* path, const cv::Rect ROI);
void CallBackFunc(int event, int x, int y, int flags, void* userdata);

int main()
{

	char title[] = "drawing line";
	
	cv::Mat image = cv::Mat::zeros(window_height, window_width,CV_8UC3);
//	MyLine(atom_image, cv::Point(0, 4*window_width/16), cv::Point(window_height, 15*window_width/16));
//	cv::imshow(atom_window,atom_image);
	cv::RNG rng(0xFFFFFF);
	//Drawing_Random_Lines(atom_image, atom_window,rng);

	cv::Rect ROI(20,20,200,200);
	cv::Mat img = ReadImage("../lena.jpg",ROI);
	img.copyTo(image(ROI));

	cv::imshow(title, image);
	cv::setMouseCallback(title, CallBackFunc, &image);
	cv::moveWindow(title,300, 50);

	while(true)
	{
		cv::imshow(title, image);
		int key = cv::waitKey(1); 
		if(key == 27)
			break;
	}
	return 0;
}

void CallBackFunc(int event, int x, int y, int flags, void* image)
{
	if (event == cv::EVENT_LBUTTONUP)
		std::cout<<"left buttion of the mouse is released- position(" <<x <<","<< y << ")"<<std::endl;
		cv::Rect ROI(x,y,x+200,y+200);
		cv::Mat img = ReadImage("../lena.jpg",ROI);
		img.copyTo((*((cv::Mat *)image))(ROI));
		
	if (event == cv::EVENT_LBUTTONDOWN)
		std::cout<<"left buttion of the mouse is clocked - position(" <<x <<","<< y << ")"<<std::endl;
	if (event == cv::EVENT_RBUTTONDOWN)
		std::cout<<"Right buttion of the mouse is clocked - position(" <<x <<","<< y << ")"<<std::endl;
	if (event == cv::EVENT_MBUTTONDOWN)
		std::cout<<"Middle buttion of the mouse is clocked - position(" <<x <<","<< y << ")"<<std::endl;
	if (event == cv::EVENT_MOUSEMOVE)
		std::cout<<"Mouse move over the window - position(" <<x <<","<< y << ")"<<std::endl;
}

cv::Mat ReadImage(const char* path, const cv::Rect ROI)
{
	cv::Mat image = cv::imread(path, cv::IMREAD_COLOR);
	cv::Mat after_resize_image;
	cv::resize(image,after_resize_image,cv::Size(ROI.width,ROI.height));
	return after_resize_image;
}

int Drawing_Random_Lines(cv::Mat img, char* window_name, cv::RNG rng)
{
	int lineType = 8;
	cv::Point pt1, pt2;

	for(int i = 0; i< 40; i++)
	{
		pt1.x = rng.uniform(0, window_width );
		pt1.y = rng.uniform(0, window_height );
		pt2.x = rng.uniform(0, window_width );
		pt2.y = rng.uniform(0, window_height );

		cv::line(img, pt1, pt2, randomColor(rng),rng.uniform(1,10),8);
		cv::imshow(window_name, img);
	}
	return 0;
}


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




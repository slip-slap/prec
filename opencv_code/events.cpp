#include <opencv2/highgui/highgui.hpp>
#include <iostream>

void CallBackFunc(int event, int x, int y, int flags, void* userdata)
{
	if (event == cv::EVENT_LBUTTONUP)
		std::cout<<"left buttion of the mouse is released- position(" <<x <<","<< y << ")"<<std::endl;
	if (event == cv::EVENT_LBUTTONDOWN)
		std::cout<<"left buttion of the mouse is clocked - position(" <<x <<","<< y << ")"<<std::endl;
	if (event == cv::EVENT_RBUTTONDOWN)
		std::cout<<"Right buttion of the mouse is clocked - position(" <<x <<","<< y << ")"<<std::endl;
	if (event == cv::EVENT_MBUTTONDOWN)
		std::cout<<"Middle buttion of the mouse is clocked - position(" <<x <<","<< y << ")"<<std::endl;
	if (event == cv::EVENT_MOUSEMOVE)
		std::cout<<"Mouse move over the window - position(" <<x <<","<< y << ")"<<std::endl;
}


int main(int argc, char** argv )
{

	cv::Mat image;
	char title[] = "name";
    image = cv::imread("../lena.jpg" , 1 );
    namedWindow(title, cv::WINDOW_NORMAL);
	cv::setMouseCallback(title, CallBackFunc, NULL);
	cv::imshow(title, image);

	cv::waitKey(0);
    return 0;
}


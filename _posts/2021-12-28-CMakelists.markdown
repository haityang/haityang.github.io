##### 用到的环境变量  

```
CMAKE_CURRENT_SOURCE_DIR  //当前源代码目录
CMAKE_CURRENT_BINARY_DIR //二进制目录
PROJECT_SOURCE_DIR //工程源目录
```



##### 编译 Release或Debug版本

```  
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake -DCMAKE_BUILD_TYPE=Release ..

```

##### 如果想引用一个framework, 需要做三件事

```
find_package(OpenGL REQUIRED)
include_directories(${OPENGL_INCLUDE_DIR})
target_link_libraries(<your program name> ${OPENGL_LIBRARIES})

```


##### 设置cmake版本  

```
cmake_minimum_required(VERSION 3.4.1)

```

##### 设置指定的C++编译器版本是必须的，如果不设置，或者为OFF，则指定版本不可用时，会使用上一版本。

```  
set(CMAKE_CXX_STANDARD_REQUIRED ON)
```


##### 设置C++17版本

```
set(CMAKE_CXX_STANDARD 17)

```

##### 指定可执行文件

```
add_executable(runtest main.cpp)

```

##### 设置编译时环境变量

```
set(CMAKE_CXX_FLAGS "-fPIC -std=c++14 -DDEBUG")
set(CMAKE_C_FLAGS "-fPIC -std=c11 -DDEBUG")

```


##### 包含头搜索路径  

```
include_directories(${PROJECT_SOURCE_DIR}/include)

```

##### 设置库搜索路径并连接库

```
link_directories(${PROJECT_SOURCE_DIR}/lib)
target_link_libraries(LightTrack -lopencv_world libncnn.a)

```


### OpenCV NCNN CMakeLists.txt

```
cmake_minimum_required(VERSION 2.8)

# define the project name
set(project_name "OpenCV3_Demo")

# set the project name
project("${project_name}")

# this is a C++11 project
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# add opencv package to the project
find_package( OpenCV REQUIRED )
INCLUDE_DIRECTORIES( ${OpenCV_INCLUDE_DIRS} ) 
SET(OpenCV_LIBRARIES ${OpenCV_LIBS})

message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

set(NCNN_FRAMEWORK_PATH ${PROJECT_SOURCE_DIR}/frameworks)
message(0 "ncnn framework path: ${NCNN_FRAMEWORK_PATH}")

add_executable(arcface "")


target_include_directories(arcface PRIVATE
  ${NCNN_FRAMEWORK_PATH}/**
  ${PROJECT_SOURCE_DIR}
)

#find custom framework
find_library(NCNN_LIB ncnn "${NCNN_FRAMEWORK_PATH}")
find_library(OPENMP_LIB openmp "${NCNN_FRAMEWORK_PATH}")
message(0 "ncnn libs path: ${NCNN_LIB}")
message(0 "openmp libs path: ${OPENMP_LIB}")



# add executable
target_sources(arcface
  PRIVATE
    "${PROJECT_SOURCE_DIR}/main.cpp"
    "${PROJECT_SOURCE_DIR}/arcface.cpp"
    "${PROJECT_SOURCE_DIR}/arcface.h"
    "${PROJECT_SOURCE_DIR}/base.cpp"
    "${PROJECT_SOURCE_DIR}/base.h"
    "${PROJECT_SOURCE_DIR}/mtcnn.cpp"
    "${PROJECT_SOURCE_DIR}/mtcnn.h"
    )



if(APPLE)
  set_target_properties(arcface PROPERTIES LINK_FLAGS "-Wl,-F${NCNN_FRAMEWORK_PATH}")
  target_link_libraries(arcface PRIVATE ${NCNN_LIB} ${OPENMP_LIB} ${OpenCV_LIBRARIES})
endif()


#SET (IMAGES ${CMAKE_SOURCE_DIR}/images/puppy.bmp ${CMAKE_SOURCE_DIR}/images/smalllogo.png ${CMAKE_SOURCE_DIR}/images/soldier.jpeg ${CMAKE_SOURCE_DIR}/images/face.mp4 ${CMAKE_SOURCE_DIR}/images/model/res10_300x300_ssd_iter_140000.caffemodel ${CMAKE_SOURCE_DIR}/images/model/deploy.prototxt)
#FILE(COPY ${IMAGES} DESTINATION .)
#FILE(COPY ${IMAGES} DESTINATION "Debug")
#FILE(COPY ${IMAGES} DESTINATION "Release")


```


### fsanet的CMakelists样例

```
cmake_minimum_required(VERSION 3.17)
project(fsanet.lite.ai.toolkit)

set(CMAKE_CXX_STANDARD 11)

# setting up lite.ai.toolkit
set(LITE_AI_DIR ${CMAKE_SOURCE_DIR}/lite.ai.toolkit)
set(LITE_AI_INCLUDE_DIR ${LITE_AI_DIR}/include)
set(LITE_AI_LIBRARY_DIR ${LITE_AI_DIR}/lib)
include_directories(${LITE_AI_INCLUDE_DIR})
link_directories(${LITE_AI_LIBRARY_DIR})

set(OpenCV_LIBS
        opencv_highgui
        opencv_core
        opencv_imgcodecs
        opencv_imgproc
        opencv_video
        opencv_videoio
        )
# add your executable
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/examples/build)

add_executable(lite_fsanet examples/test_lite_fsanet.cpp)
target_link_libraries(lite_fsanet
        lite.ai.toolkit
        onnxruntime
        MNN  # need, if built lite.ai.toolkit with ENABLE_MNN=ON,  default OFF
        ncnn # need, if built lite.ai.toolkit with ENABLE_NCNN=ON, default OFF
        TNN  # need, if built lite.ai.toolkit with ENABLE_TNN=ON,  default OFF
        ${OpenCV_LIBS})  # link lite.ai.toolkit & other libs.


```
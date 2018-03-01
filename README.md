#SDWebImage替换为Kingfisher
##需要增加的地方
1.
引用的地方增加```import Kingfisher```
2.
podfile增加
```
#图片加载swift库Kingfisher放在了BasicServiceProject
  pod 'BasicServiceProject','0.5.x'#版本号目前未知
```

##需要替换的地方

>**SDWebImage函数**
	- (void)`sd_setImageWithURL`:(NSURL *)url;
	- (void)`sd_setImageWithURL`:(NSURL *)url `placeholderImage`:(UIImage *)placeholder;
	- (void)`sd_setImageWithURL`:(NSURL *)url `placeholderImage`:(UIImage *)placeholder `options`:(SDWebImageOptions)options;
	- (void)`sd_setImageWithURL`:(NSURL *)url `completed`:(SDWebImageCompletionBlock)completedBlock;
	typedef void(^`SDWebImageCompletionBlock`)(UIImage *`image`, NSError *`error`, SDImageCacheType `cacheType`, NSURL *`imageURL`);
	
替换为
>**Kingfisher**
	`public func` setImage(with `resource`: Resource?, `placeholder`: Placeholder? = nil, `options`: KingfisherOptionsInfo? = nil, `progressBlock`: DownloadProgressBlock? = nil,  `completionHandler`: CompletionHandler? = nil) -> `RetrieveImageTask`
                         
###需要注意的问题

###1.SDImageCacheType

```
typedef void(^SDWebImageCompletionBlock)(UIImage *image, NSError *error, SDImageCacheType cacheType, NSURL *imageURL);
```
替换为
```
public typealias CompletionHandler = ((_ image: Image?, _ error: NSError?, _ cacheType: CacheType, _ imageURL: URL?) -> Void)
```

例1
```
var refeshHeightClosure: ((UIImage?, Error?, SDImageCacheType, URL?) -> Void)? = nil
```
替换为
```
var refeshHeightClosure: ((UIImage?, Error?, _ cacheType: CacheType, URL?) -> Void)? = nil
```

例2
```
self.iconView.sd_setImage(with: imgUrl, placeholderImage: placeHorderImg, options: SDWebImageOptions.retryFailed) {[weak self] (img, error, type, url) in
```
替换为
```
self.iconView.kf.setImage(with: imgUrl, placeholder: placeHorderImg) {[weak self] (img, error, type, url) in
```

或者
```
imageView.sd_setImage(with: entity.userImageList[index], placeholderImage: img, options: SDWebImageOptions.cacheMemoryOnly, completed: { (image: UIImage?, error : Error?, cacheType : SDImageCacheType, imageURL :URL?) in
```
替换为
```
imageView.kf.setImage(with: imgUrl, placeholder: placeHorderImg) {[weak self] (image: UIImage?, error : Error?, cacheType: CacheType , imageURL :URL?) in
```

####[这里](https://github.com/doreamongit/SDToKF/blob/master/Kingfisher.py)我编写了一个脚本方便大家对各自负责项目的替换
###用法
1.下载[Kingfisher.py](https://github.com/doreamongit/SDToKF/blob/master/Kingfisher.py)，
2.赋权
```
chmod 777 /Users/damon/Downloads/Kingfisher.py
```

3.使用，前边是Kingfisher.py脚本的路径，后边是要执行的项目的路径
```
/Users/damon/Downloads/Kingfisher.py /Users/damon/Documents/work/program/iOS/sunland/sdjgactivityoperationproject
```
4.使用```Kingfisher.py```脚本的问题汇总
>4.1由于脚本是基于```fileinput```库一行行读取文本的，所以如果要替换的```sd_setImage...```函数包含```换行```的话会失败
>4.2```SDWebImageOptions(rawValue:0)```这样的```SDWebImageOptions```未处理，需自己手动删掉
>4.3由于Kingfisher的```KingfisherOptionsInfoItem```枚举不包含```SDWebImageRetryFailed```类型，所以检测设置```SDWebImageOptions.retryFailed```或```.retryFailed```的地方对应换成了```空字符串```
>4.4```SDWebImageOptions.refreshCached```或```.refreshCached```对应换成了```[.forceRefresh]```





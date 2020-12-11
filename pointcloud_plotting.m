%%
pc5 = load('pointclouds/point_cloud_5.mat')

single_example = pc5.Results6{1,1}.Location
single_example(:,3) = - single_example(:,3) + 1.1
pcshow(single_example)
% this one is reconstructed depth from calibrated stereo ir images
% https://projects.asl.ethz.ch/datasets/doku.php?id=2018plantstressphenotyping

save('testcloud_realcrop.mat','single_example');

%%



%%

pred = pcread('cloud_vis/3class_pred_cloud.pcd');
truth = pcread('cloud_vis/3class_truth_cloud.pcd');
error = pcread('cloud_vis/3class_error_cloud.pcd');
real = pcread('cloud_vis/realworld_pred_cloud_3c.pcd');

indx = find(~all(error.Color==0,2));
error_cloud = pointCloud(error.Location(indx,:));
nr_points = size(indx,1);
error_cloud.Color = uint8(repmat([255,0,0],nr_points,1));

%shifted_vector = truth.Location;
%shifted_vector(:,1) = truth.Location(:,1) + 1.2;
%shifted_vector(:,3) = truth.Location(:,1) + 1.2;
%shifted_truth = pointCloud(shifted_vector);
%shifted_truth.Color = truth.Color

%%
figure;
pcshow(pred, 'MarkerSize', 15);
view(90,0)
set(gca,'visible','off')
figure;
pcshow(truth, 'MarkerSize', 15);
view(90,0)
set(gca,'visible','off')
figure;
pcshow(error_cloud, 'MarkerSize', 15);
view(90,0)
set(gca,'visible','off')

%%
figure;
pcshow(pred, 'MarkerSize', 15);
view(44.0977, 88.8877)
zoom(3)
set(gca,'visible','off')
figure;
ha = pcshow(truth, 'MarkerSize', 15);
view(44.0977, 88.8877)
zoom(3)
set(gca,'visible','off')
figure;
ha = pcshow(error_cloud, 'MarkerSize', 50);
view(44.0977, 88.8877)
zoom(3)
set(gca,'visible','off')

%%
figure;
pcshow(real, 'MarkerSize', 15);
view(90,0)
set(gca,'visible','off')

figure;
pcshow(real, 'MarkerSize', 15);
view(44.0977, 88.8877)
zoom(3)
set(gca,'visible','off')
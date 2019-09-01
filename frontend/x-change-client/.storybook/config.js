import { configure } from '@storybook/react';
import '../src/sass/_main.scss';

const req = require.context('../src/stories', true, /\.stories\.tsx$/);
function loadStories() {
  req.keys().forEach(filename => req(filename));
}

configure(loadStories, module);

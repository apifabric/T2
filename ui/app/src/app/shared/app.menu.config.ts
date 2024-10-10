import { MenuRootItem } from 'ontimize-web-ngx';

import { AddressCardComponent } from './Address-card/Address-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { CustomerInsightCardComponent } from './CustomerInsight-card/CustomerInsight-card.component';

import { LoyaltyProgramCardComponent } from './LoyaltyProgram-card/LoyaltyProgram-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Address', name: 'ADDRESS', icon: 'view_list', route: '/main/Address' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'CustomerInsight', name: 'CUSTOMERINSIGHT', icon: 'view_list', route: '/main/CustomerInsight' }
    
        ,{ id: 'LoyaltyProgram', name: 'LOYALTYPROGRAM', icon: 'view_list', route: '/main/LoyaltyProgram' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AddressCardComponent

    ,CustomerCardComponent

    ,CustomerInsightCardComponent

    ,LoyaltyProgramCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

];